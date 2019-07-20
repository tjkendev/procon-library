require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'

class Canonical < Extensions::Postprocessor

  def add_canonical document, output, url
    return output unless document.attributes.key? 'baseurl'

    c_url = document.attributes['baseurl'] + url

    doc = Nokogiri::HTML.parse(output)
    doc.search("head").each {|el|
        el.add_child "<link rel=\"canonical\" href=\"#{c_url}\" />"
    }
    doc.to_html
  end

  def process document, output
    return output if !document.attributes.key? 'relpath'

    # :canonical-lang: が定義 -> 別のプログラム言語ページが優先
    if document.attributes.key? 'canonical-lang'
        lang = document.attributes['canonical-lang']
        url = document.attributes['relpath'].sub(/^[^\/]+\//, "#{lang}/")
        return add_canonical document, output, url
    end

    # :canonical: が定義 -> このサイトの特定の相対パスが優先
    if document.attributes.key? 'canonical'
      url = document.attributes['canonical']
      return add_canonical document, output, url
    end

    return output
  end
end