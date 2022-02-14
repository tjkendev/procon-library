RUBY_ENGINE == 'opal' ? (require 'custom-page/extension') : (require_relative 'custom-page/extension')
RUBY_ENGINE == 'opal' ? (require 'ogp/extension') : (require_relative 'ogp/extension')
RUBY_ENGINE == 'opal' ? (require 'relative-path/extension') : (require_relative 'relative-path/extension')
RUBY_ENGINE == 'opal' ? (require 'canonical/extension') : (require_relative 'canonical/extension')

Extensions.register do
  preprocessor RelativePathPreprocessor

  if (@document.basebackend? 'html')
    treeprocessor CustomPageTreeprocessor
    treeprocessor OGPHeaderTreeprocessor

    postprocessor OGPHeaderPostprocessor
    postprocessor OGPDescriptionPostprocessor
    postprocessor CustomPagePostprocessor
    postprocessor CanonicalPostprocessor
  end

  inline_macro OGPLinkInlineMacroProcessor
end