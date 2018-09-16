.PHONY: pages

CMD := asciidoctor-latex
FORMAT := html
SRC := ./page-src
DST := ./page
TARGET := '**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
STYLESDIR := https://tjkendev.github.io/procon-library/doc-src/

pages:
	$(CMD) -b $(FORMAT) -R $(SRC) -D $(DST) $(TARGET) -B ./ -a source-highlighter=$(HIGHLIGHTER) -a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(STYLESDIR)
