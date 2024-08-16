# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "esc190-notes"
  spec.version       = "0.0.0"
  spec.authors       = ["Youssef Rachad"]
  spec.email         = [""]
  spec.license       = ""
  spec.homepage      = "https://github.com/Youssef-Rachad/ESC180_ESC190_notes"
  spec.summary       = "Course Notes for ESC190: Computer Algorithms and Data Structures."

  spec.license       = " "
  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_data|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.3"
  spec.add_runtime_dependency "jekyll-seo-tag"
end
