RUBY_ENGINE == 'opal' ? (require 'custom-page/extension') : (require_relative 'custom-page/extension')
RUBY_ENGINE == 'opal' ? (require 'ogp/extension') : (require_relative 'ogp/extension')
RUBY_ENGINE == 'opal' ? (require 'relative-path/extension') : (require_relative 'relative-path/extension')

Extensions.register do
  preprocessor OGP
  preprocessor RelativePath

  if (@document.basebackend? 'html')
    postprocessor OGPHeader
    postprocessor OGPDescription

    postprocessor CustomPage
  end

  inline_macro OGPLinkMacro
end