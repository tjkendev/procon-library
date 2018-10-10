require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'

class CustomPage < Extensions::Postprocessor
  def process document, output
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