
RUBY_ENGINE == 'opal' ? (require 'ogp/extension') : (require_relative 'ogp/extension')

Extensions.register do
  preprocessor OGP

  if (@document.basebackend? 'html')
    postprocessor OGPHeader
  end
end