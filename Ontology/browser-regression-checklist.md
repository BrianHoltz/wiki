# Ontology browser regression checklist

- [ ] Canonical browser loads `Ontology` data with `Entity`, `Property`, and `Relation` at the top level.
- [ ] Historical SUMO browser loads the pre-extension `Entity` tree.
- [ ] Root and first-level nodes open by default.
- [ ] Triangle controls toggle only between collapsed and expanded states.
- [ ] Alternate-parent and alternate-child lines are hidden while their node is collapsed.
- [ ] The `↖` control sits immediately after the node title.
- [ ] Lineage mode shows every ancestor through the selected node and only its direct children.
- [ ] Lineage mode hides descendants below those direct children and alternate-parent projections.
- [ ] Child counts show direct plus deeper descendants and omit zero values.
- [ ] Definitions begin after the title metadata and truncate with an ellipsis.
- [ ] Expand and Collapse controls affect the full tree.
- [ ] Search results open the complete ancestor chain and scroll to the matched node.
- [ ] Search-result links open the matched node in diamond lineage mode.
- [ ] Preset search buttons populate the search box and immediately open their target in diamond lineage mode.
- [ ] The count summary is a normal link to `Ontology.md`.
