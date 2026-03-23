#!/usr/bin/env python3
"""
Heuristic speaker diarization for a two-speaker interview transcript.
Input:  single-line Whisper text blob
Output: Markdown with **A.J.:** and **Hogan:** speaker turns

Usage: python3 diarize.py Hogan.txt Hogan_diarized.md
"""
import re
import sys


def split_sentences(text):
    """Split on sentence-ending punctuation followed by a space."""
    # Insert newline after . ? ! when followed by whitespace + capital or quote
    text = re.sub(r'([.?!])\s+(?=[A-Z"\'])', r'\1\n', text)
    parts = [s.strip() for s in text.split('\n') if s.strip()]
    return parts


# Patterns that strongly suggest A.J. (the host)
AJ_PATTERNS = [
    r'^\s*(sure|right|yeah|yep|okay|ok|correct|absolutely|interesting|'
    r'fascinating|amazing|wow|really|i see|great|no|i know|'
    r"that's right|of course|exactly|hm+|oh|ah|i didn'?t know|"
    r'unbelievable|wonderful|cool|nice|gotcha|fair enough|true|'
    r'and so|but|so)\s*[.,!]?\s*$',           # bare affirmations
    r'\?\s*$',                                  # questions
    r"^let'?s\b",                               # "let's take a break"
    r"^we'?ll\b",                               # "we'll be right back"
    r'^(do|can|could|would|have|has|did|is|are|was|were|will)\s+you\b',
    r'^(what|how|where|why|who|when|which)\b',
    r'^(so|and|but)\s+(you|did|do|is|are|was|were|have|the)',
    r'^i want to\b',
    r'^tell me\b',
    r"^that'?s (a|the|very|quite|really|an)\b",
    r'^now,?\s+(let|i|we|tell)',
    r'^last question\b',
    r'^one (last|more|other)\b',
    r"^i'?m\s+(going|curious|interested|fascinated|blown)",
    r'^so\s+just\s+to\b',
    r'^just\s+(to\s+set|for\s+those|to\s+be)\b',
]

# Patterns that strongly suggest Hogan (the guest)
HOGAN_PATTERNS = [
    r'\bwe believe\b',
    r'\bthe (templar )?order\b',
    r'\btemplar\b',
    r'\baccording to (our|the)\b',
    r'\bmonoatomic\b',
    r'\balchemy\b',
    r'\balchemical\b',
    r'\bgnostic\b',
    r'\bgnosis\b',
    r'\batlantis\b',
    r'\buthlant\b',
    r'\batlantean\b',
    r'\bpyramid\b',
    r'\bhieroglyph\b',
    r'\bpharaoh\b',
    r"\bin our (records|tradition|belief|order'?s)\b",
    r'\bso the templar\b',
    r'\bwhat (that|this|the|it) (was|is|means|meant)\b',
    r'\bfor example,\b.*\btempl',
    r'\bby the way,\b',
    r"\bhere'?s (what|where|why|how)\b",
]

AJ_COMPILED = [re.compile(p, re.IGNORECASE) for p in AJ_PATTERNS]
HOGAN_COMPILED = [re.compile(p, re.IGNORECASE) for p in HOGAN_PATTERNS]


def score(sentence):
    """
    Positive = A.J., negative = Hogan.
    """
    s = sentence.strip()
    words = s.split()
    n = len(words)
    sc = 0

    # Length heuristic: short = host, long = guest
    if n <= 3:
        sc += 4
    elif n <= 6:
        sc += 2
    elif n <= 10:
        sc += 1
    elif n >= 25:
        sc -= 2
    elif n >= 40:
        sc -= 3

    # Pattern matching
    for pat in AJ_COMPILED:
        if pat.search(s):
            sc += 3
            break  # one match is enough

    for pat in HOGAN_COMPILED:
        if pat.search(s):
            sc -= 3
            break

    return sc


def assign_speakers(sentences):
    scores = [score(s) for s in sentences]
    speakers = []
    current = 'AJ'  # host always opens

    for i, (s, sc) in enumerate(zip(sentences, scores)):
        if sc >= 4:
            current = 'AJ'
        elif sc <= -3:
            current = 'Hogan'
        elif sc >= 3 and current == 'Hogan':
            current = 'AJ'
        elif sc <= -2 and current == 'AJ':
            current = 'Hogan'
        # else: stay with current speaker

        speakers.append(current)

    return speakers


def group_turns(sentences, speakers):
    turns = []
    if not sentences:
        return turns
    cur_sp = speakers[0]
    cur_buf = [sentences[0]]
    for s, sp in zip(sentences[1:], speakers[1:]):
        if sp == cur_sp:
            cur_buf.append(s)
        else:
            turns.append((cur_sp, ' '.join(cur_buf)))
            cur_sp = sp
            cur_buf = [s]
    turns.append((cur_sp, ' '.join(cur_buf)))
    return turns


def to_markdown(turns):
    lines = []
    for speaker, text in turns:
        label = '**A.J.:**' if speaker == 'AJ' else '**Hogan:**'
        lines.append(f'{label} {text}\n')
    return '\n'.join(lines)


def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} input.txt output.md')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        text = f.read()

    sentences = split_sentences(text)
    speakers = assign_speakers(sentences)
    turns = group_turns(sentences, speakers)
    md = to_markdown(turns)

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(md)

    aj = sum(1 for sp, _ in turns if sp == 'AJ')
    ho = sum(1 for sp, _ in turns if sp == 'Hogan')
    print(f'{len(sentences)} sentences → {len(turns)} turns  (A.J.: {aj}, Hogan: {ho})')


if __name__ == '__main__':
    main()
