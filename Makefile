.PHONY: docs docs-local clean

BASEPATH = https://tjkendev.github.io/procon-library/

CMD := bundle exec asciidoctor-latex
FMT := html
SRC := ./docs/src
DST := ./docs
DSTSUBDIR := docs/python docs/cpp docs/other
BASE := ./
ASRC := $(shell readlink -f $(SRC))/
TARGET := 'docs/**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
SRCDIR := '$(BASEPATH)src'
STATICDIR := '$(BASEPATH)static'
TITLE := "yaketake08's 実装メモ"
SGEN-CMD := bundle exec ruby ./docs/src/sitemap-generator.rb


# for local debug
CUR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DST-LOCAL := ./docs-local
SRCDIR-LOCAL := '$(CUR)/docs/src'
STATICDIR-LOCAL := '$(CUR)/docs/static'

docs:
	@$(CMD) -b $(FMT) -R $(SRC) -D $(DST) $(TARGET) -B $(BASE) \
		-r ./docs/src/lib/custom-extensions.rb \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(STATICDIR) \
		-a jsdir=$(STATICDIR) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL) \
		-a basedir=$(ASRC) -a baseurl=$(BASEPATH) \
		-a nofooter -a inject_javascript=no -a lang=ja \
		-a attribute-missing=warn --failure-level=WARN
	@$(SGEN-CMD) $(BASEPATH) $(SRC) $(DST)

docs-local:
	$(CMD) -b $(FMT) -R $(SRC) -D $(DST-LOCAL) $(TARGET) -B $(BASE) \
		-r ./docs/src/lib/custom-extensions.rb \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(STATICDIR-LOCAL) \
		-a jsdir=$(STATICDIR-LOCAL) -a docinfo1 -a docinfodir=$(SRCDIR-LOCAL) \
		-a basedir=$(ASRC) -a baseurl=$(BASEPATH) \
		-a nofooter -a inject_javascript=no -a lang=ja \
		-a attribute-missing=warn --failure-level=WARN
	$(SGEN-CMD) $(BASEPATH) $(SRC) $(DST-LOCAL)

clean:
	rm -f ./docs/index.html ./docs/sitemap.xml
	rm -rf $(DSTSUBDIR)
	rm -rf $(DST-LOCAL)
