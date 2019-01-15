require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'
require 'opengraph_parser'
require 'cgi'

class CustomPage < Extensions::Postprocessor
  def process document, output

    # :no-copy: が定義されている場合はボタンを生成しない
    if document.attributes['no-copy']
      return output
    end

    doc = Nokogiri::HTML.parse(output)

    # add "Copy to clipboard" button
    doc.search(".listingblock").each_with_index{|el, i|
      code = el.search("code")
      code.add_class("code-idx-%d" % i)
      el.prepend_child '<button type="button" class="copy-btn" data-clipboard-target=".code-idx-%d">Copy to clipboard</button>' % i
    }

    doc.to_html
  end
end

class OGPLinkMacro < Extensions::InlineMacroProcessor
  use_dsl

  named :dlink

  def process parent, target, attributes
    doc = parent.document
    og = OpenGraph.new(target)
    title = og.title || target
    %(<a href="#{target}">#{title}</a>)
  end
end