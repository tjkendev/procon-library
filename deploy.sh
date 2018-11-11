cd ./docs
find ./src -type f -name '*.adoc' -delete
rm -rf ./src/lib
rm -f ./src/docinfo.html
git init
git add .
git commit -m "commit on `date "+%Y-%m-%d %H:%M:%S"`"
git push -f git@github.com:tjkendev/procon-library.git master:gh-pages
