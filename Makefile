.PHONY: docs docs-local clean

CMD := asciidoctor-latex
FMT := html
SRC := ./docs/src
DST := ./docs
DSTSUBDIR := docs/python docs/cpp
BASE := ./
TARGET := '**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
SRCDIR := 'https://tjkendev.github.io/procon-library/src'
TITLE := '実装メモ'


# for local debug
CUR := '$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))'
DST-LOCAL := ./docs-local
SRCDIR-LOCAL := $(CUR)/docs/src/

docs:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST) $(TARGET) -B $(BASE) \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(SRCDIR) \
		-a jsdir=$(SRCDIR) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL)

docs-local:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST-LOCAL) $(TARGET) -B $(BASE) \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(SRCDIR-LOCAL) \
		-a jsdir=$(SRCDIR-LOCAL) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL)

clean:
	rm -f ./docs/index.html
	rm -rf $(DSTSUBDIR)
	rm -rf $(DST-LOCAL)
