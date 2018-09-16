.PHONY: doc

CMD := asciidoctor-latex
FORMAT := html
SRC := ./doc-src
DST := ./doc
TARGET := '**/*.adoc'
HIGHLIGHTER := highlightjs
STYLESHEET := ./stylesheet/github.css
STYLESDIR := https://tjkendev.github.io/procon-library/doc-src/

doc:
	$(CMD) -b $(FORMAT) -R $(SRC) -D $(DST) $(TARGET) -B ./ -a source-highlighter=$(HIGHLIGHTER) -a stylesheet=$(STYLESHEET) -a linkcss -a stylesdir=$(STYLESDIR)
