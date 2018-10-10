require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

class OGP < Extensions::Preprocessor
  def process document, reader
    doc_attrs = document.attributes

    basedir = doc_attrs['basedir']
    docfile = doc_attrs['docfile']
    docfilesuffix = doc_attrs['docfilesuffix']
    outfilesuffix = doc_attrs['outfilesuffix']

    docfile.slice! basedir

    dirname = File.dirname(docfile)
    filename = File.basename(docfile, docfilesuffix)

    if dirname == '.' && filename == 'index'
      doc_attrs['og-desc'] = 'トップページ'
      doc_attrs['og-type'] = 'website'
    else
      # update 'og-desc' when 'doctitle' is updated
      def doc_attrs.[]=(k, v)
        super k, v
        if k == 'doctitle'
          super 'og-desc', v
        end
      end
      doc_attrs['og-type'] = 'article'
    end

    nil
  end
end

class OGPHeader < Extensions::Postprocessor
  def process document, output
    output.sub "<head>", "<head prefix=\"og: http://ogp.me/ns# website: http://ogp.me/ns/website#\">"
  end
end