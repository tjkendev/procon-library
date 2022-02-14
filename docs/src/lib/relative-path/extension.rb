require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

class RelativePathPreprocessor < Extensions::Preprocessor
  def process document, reader
    attrs = document.attributes

    basedir = attrs['basedir']
    docfile = attrs['docfile']
    docfilesuffix = attrs['docfilesuffix']
    outfilesuffix = attrs['outfilesuffix']

    docfile.slice! basedir

    dirname = File.dirname(docfile)
    filename = File.basename(docfile, docfilesuffix) + outfilesuffix

    if dirname == '.'
      relpath = filename
    else
      relpath = dirname + '/' + filename
    end
    attrs['relpath'] = relpath

    nil
  end
end