.PHONY: pages pages-local clean

CMD := asciidoctor-latex
FMT := html
SRC := ./page-src
DST := ./page
BASE := ./
TARGET := '**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
SRCDIR := 'https://tjkendev.github.io/procon-library/page-src/'
TITLE := '実装メモ'

# for local debug
CUR := '$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))'
DST-LOCAL := ./page-local
SRCDIR-LOCAL := $(CUR)/page-src/

pages:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST) $(TARGET) -B $(BASE) \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(SRCDIR) \
		-a jsdir=$(SRCDIR) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL)

pages-local:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST-LOCAL) $(TARGET) -B $(BASE) \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(SRCDIR-LOCAL) \
		-a jsdir=$(SRCDIR-LOCAL) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL)

clean:
	rm -rf $(DST)
	rm -rf $(DST-LOCAL)
