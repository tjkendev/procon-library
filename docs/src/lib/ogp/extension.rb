require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'

class OGPHeaderTreeprocessor < Extensions::Treeprocessor
  def process document
    basedir = document.attr 'basedir'
    docfile = document.attr 'docfile'
    docfilesuffix = document.attr 'docfilesuffix'
    outfilesuffix = document.attr 'outfilesuffix'

    docfile.slice! basedir

    dirname = File.dirname(docfile)
    filename = File.basename(docfile, docfilesuffix)

    if dirname == '.' && filename == 'index'
      document.set_attr 'og-desc', 'トップページ'
      document.set_attr 'og-type', 'website'
    else
      document.set_attr 'og-desc', document.attr('doctitle')
      document.set_attr 'og-type', 'article'
    end

    document
  end
end

class OGPHeaderPostprocessor < Extensions::Postprocessor
  def process document, output
    output.sub "<head>", "<head prefix=\"og: http://ogp.me/ns# website: http://ogp.me/ns/website#\">"
  end
end

class OGPDescriptionPostprocessor < Extensions::Postprocessor
  def process document, output
      doc = Nokogiri::HTML.parse(output)
      body = doc.search("#content").text.gsub(/\n+/, ' ')

      text = body.slice(0, 100).strip + "..."
      doc.search("meta[name=\"description\"]").attr("content", text)
      doc.to_html
  end
end