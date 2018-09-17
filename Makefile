.PHONY: pages

CMD := asciidoctor-latex
FORMAT := html
SRC := ./page-src
DST := ./page
BASE := ./
TARGET := '**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
STYLESDIR := https://tjkendev.github.io/procon-library/page-src/
TITLE := 'yaketake08の競プロ実装置き場'

pages:
	$(CMD) -b $(FORMAT) -R $(SRC) -D $(DST) $(TARGET) -B $(BASE) \
		-a pagetitle=$(TITLE) -a source-highlighter=$(HIGHLIGHTER) \
		-a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(STYLESDIR)
