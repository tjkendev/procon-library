require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'

class CanonicalPostprocessor < Extensions::Postprocessor

  def add_canonical document, output, url
    return output unless document.attr? 'baseurl'

    c_url = document.attr('baseurl') + url

    doc = Nokogiri::HTML.parse(output)
    doc.search("head").each {|el|
        el.add_child "<link rel=\"canonical\" href=\"#{c_url}\" />"
    }
    doc.to_html
  end

  def process document, output
    return output if !document.attr? 'relpath'

    # :canonical-lang: が定義 -> 別のプログラム言語ページが優先
    if document.attributes.key? 'canonical-lang'
      lang = document.attr 'canonical-lang'
      url = document.attr('relpath').sub(/^[^\/]+\//, "#{lang}/")
      return add_canonical document, output, url
    end

    # :canonical: が定義 -> このサイトの特定の相対パスが優先
    if document.attr? 'canonical'
      url = document.attr 'canonical'
      return add_canonical document, output, url
    end

    # canonicalが未指定 -> サイトのURLをそのまま指定
    url = document.attr 'relpath'
    return add_canonical document, output, url
  end
end