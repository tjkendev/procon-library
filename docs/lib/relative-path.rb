RUBY_ENGINE == 'opal' ? (require 'relative-path/extension') : (require_relative 'relative-path/extension')

Extensions.register do
  preprocessor RelativePath
end