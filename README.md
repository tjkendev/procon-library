# procon-library

[![Build Status](https://app.travis-ci.com/tjkendev/procon-library.svg?branch=master)](https://app.travis-ci.com/tjkendev/procon-library)

競技プログラミング参照用のテンプレートやライブラリ等の置き場

* Webページ: <https://tjkendev.github.io/procon-library/>

## ページ生成方法

### 依存

* Ruby 2.7.3
* [Asciidoctor Latex](https://github.com/asciidoctor/asciidoctor-latex)

### 準備

```sh
# install dependencies from Gemfile
$ bundle install
```

### ページ生成

```sh
# generate output files in 'docs-local' for development
$ make docs-local
# generate output files in 'docs' for production
$ make docs
```

## ページ生成について

* [競プロライブラリのページをAsciiDocで作った話](https://smijake3.hatenablog.com/entry/2018/12/13/224443)
