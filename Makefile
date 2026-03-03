WIKI_DIR := $(shell pwd)
REMOTE   := holtzorg@holtz.org:~/public_html/Thoughts/wiki/
EXCLUDES := $(HOME)/rsync_excludes

.PHONY: build deploy

build:
	python3 build.py

deploy: build
	rsync -lPOvrt --delete-after --delete-excluded \
	  --modify-window=60 \
	  --exclude-from $(EXCLUDES) \
	  $(WIKI_DIR)/ $(REMOTE)
