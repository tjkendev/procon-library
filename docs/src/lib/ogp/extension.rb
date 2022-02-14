require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'

class OGPHeaderTreeprocessor < Extensions::Treeprocessor
  def process document
    attrs = document.attributes

    basedir = attrs['basedir']
    docfile = attrs['docfile']
    docfilesuffix = attrs['docfilesuffix']
    outfilesuffix = attrs['outfilesuffix']

    docfile.slice! basedir

    dirname = File.dirname(docfile)
    filename = File.basename(docfile, docfilesuffix)

    if dirname == '.' && filename == 'index'
      attrs['og-desc'] = 'トップページ'
      attrs['og-type'] = 'website'
    else
      attrs['og-desc'] = attrs['doctitle']
      attrs['og-type'] = 'article'
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