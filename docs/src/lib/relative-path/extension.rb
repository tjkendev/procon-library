require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

class RelativePathPreprocessor < Extensions::Preprocessor
  def process document, reader
    basedir = document.attr 'basedir'
    docfile = document.attr 'docfile'
    docfilesuffix = document.attr 'docfilesuffix'
    outfilesuffix = document.attr 'outfilesuffix'

    docfile.slice! basedir

    dirname = File.dirname(docfile)
    filename = File.basename(docfile, docfilesuffix) + outfilesuffix

    if dirname == '.'
      relpath = filename
    else
      relpath = dirname + '/' + filename
    end
    document.set_attr 'relpath', relpath

    nil
  end
end