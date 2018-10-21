.PHONY: docs docs-local clean

BASEPATH = https://tjkendev.github.io/procon-library/

CMD := asciidoctor-latex
FMT := html
SRC := ./docs/src
DST := ./docs
DSTSUBDIR := docs/python docs/cpp
BASE := ./
ASRC := $(shell readlink -f $(SRC))/
TARGET := '**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
SRCDIR := '$(BASEPATH)src'
TITLE := "yaketake08's 実装メモ"


# for local debug
CUR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DST-LOCAL := ./docs-local
SRCDIR-LOCAL := '$(CUR)/docs/src'

docs:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST) $(TARGET) -B $(BASE) \
		-r ./docs/lib/relative-path.rb \
		-r ./docs/lib/ogp.rb \
		-r ./docs/lib/custom-page.rb \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(SRCDIR) \
		-a jsdir=$(SRCDIR) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL) \
		-a basedir=$(ASRC) -a baseurl=$(BASEPATH) \
		-a attribute-missing=warn --failure-level=WARN


docs-local:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST-LOCAL) $(TARGET) -B $(BASE) \
		-r ./docs/lib/relative-path.rb \
		-r ./docs/lib/ogp.rb \
		-r ./docs/lib/custom-page.rb \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(SRCDIR-LOCAL) \
		-a jsdir=$(SRCDIR-LOCAL) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL) \
		-a basedir=$(ASRC) -a baseurl=$(BASEPATH) \
		-a attribute-missing=warn --failure-level=WARN

clean:
	rm -f ./docs/index.html
	rm -rf $(DSTSUBDIR)
	rm -rf $(DST-LOCAL)
