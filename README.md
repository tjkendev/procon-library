procon-library
====

## 概要

競技プログラミングで参照できるテンプレートやライブラリ等の置き場

* webページ: [http://tjkendev.github.io/procon-library/](http://tjkendev.github.io/procon-library/)

## コンパイル

### 依存

* [Asciidoctor Latex](https://github.com/asciidoctor/asciidoctor-latex)

### インストール

```sh
# install Asciidoctor Latex
$ gem install asciidoctor-latex --pre

# need for Asciidoctor extension
$ gem install nokogiri opengraph_parser
```

### コンパイル

```sh
# generate (local test) HTML files in 'docs-local'
$ make docs-local
# generate HTML files in 'docs'
$ make docs
```
