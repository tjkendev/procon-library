require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

class RelativePath < Extensions::Preprocessor
  def process document, reader
    doc_attrs = document.attributes

    basedir = doc_attrs['basedir']
    docfile = doc_attrs['docfile']
    docfilesuffix = doc_attrs['docfilesuffix']
    outfilesuffix = doc_attrs['outfilesuffix']

    docfile.slice! basedir

    dirname = File.dirname(docfile)
    filename = File.basename(docfile, docfilesuffix) + outfilesuffix

    if dirname == '.'
      relpath = filename
    else
      relpath = dirname + '/' + filename
    end
    doc_attrs['relpath'] = relpath

    nil
  end
end