WIKI_DIR  := $(shell pwd)
# Canonical deploy for the markdown wiki tree (managed separately from site-wide rsync).
REMOTE    := holtzorg@holtz.org:~/public_html/Thoughts/wiki/
ROOT_DIR  := $(WIKI_DIR)/../..
ROOT_REMOTE := holtzorg@holtz.org:~/public_html/
EXCLUDES  := $(HOME)/bin/rsync_excludes

.PHONY: build deploy redirect

build:
	python3 BrianThinks.py

deploy: build
	rsync -lPOvrt --delete-after --delete-excluded \
	  --modify-window=60 \
	  --exclude-from $(EXCLUDES) \
	  $(WIKI_DIR)/ $(REMOTE)

redirect:
	rsync -lPOvt \
	  $(ROOT_DIR)/.htaccess \
	  $(ROOT_REMOTE)
