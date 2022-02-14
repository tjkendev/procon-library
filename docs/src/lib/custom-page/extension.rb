require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include Asciidoctor

require 'nokogiri'
require 'opengraph_parser'
require 'cgi'

class CustomPageTreeprocessor < Extensions::Treeprocessor
  def process document
    attrs = document.attributes

    if !attrs.key?("title")
      # set the page's title
      doctitle = attrs["doctitle"]
      pagetitle = attrs["pagetitle"]

      if !doctitle.empty? && !pagetitle.empty?
        attrs["title"] = "#{doctitle} - #{pagetitle}"
      end
    end

    document
  end
end

class CustomPagePostprocessor < Extensions::Postprocessor
  def process document, output
    doc = Nokogiri::HTML.parse(output)

    if !document.attributes.key?('no-copy')
      # :no-copy: が定義されていなければボタンを生成する

      # add "Copy to clipboard" button
      doc.search(".listingblock").each_with_index{|el, i|
        code = el.search("code")
        code.add_class("code-idx-%d" % i)
        el.prepend_child '<button type="button" class="copy-btn" data-clipboard-target=".code-idx-%d">Copy to clipboard</button>' % i
      }
    end

    contents = doc.search("#content").first
    if !document.attributes.key?('no-back')
      # add a back button
      contents.add_child '<hr />'
      bb_section = Nokogiri::XML::Node::new('div', doc)
      bb_section.add_class 'sect1'
      bb_section.inner_html = '<p><a href="../index.html">戻る</a></p>'

      contents.add_child bb_section
    end

    # docinfo-last.html
    docinfo_last = document.docinfo "last"
    if !docinfo_last.empty?
      doc.at("body").add_child(docinfo_last)
    end

    doc.to_html
  end
end

class OGPLinkInlineMacroProcessor < Extensions::InlineMacroProcessor
  use_dsl

  named :dlink

  def process parent, target, attributes
    doc = parent.document
    og = OpenGraph.new(target)
    title = og.title || target
    %(<a href="#{target}">#{title}</a>)
  end
end