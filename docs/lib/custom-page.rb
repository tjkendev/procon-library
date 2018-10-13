RUBY_ENGINE == 'opal' ? (require 'custom-page/extension') : (require_relative 'custom-page/extension')

Extensions.register do
  if (@document.basebackend? 'html')
    postprocessor CustomPage
  end

  inline_macro OGPLinkMacro
end