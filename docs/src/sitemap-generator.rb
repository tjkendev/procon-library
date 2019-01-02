# the script for generating sitemap.xml
require 'find'
require 'fileutils'

result = ["<?xml version='1.0' encoding='UTF-8' ?>
<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"]

base_url = ARGV[0]
base_dir = ARGV[1]

if !base_url || !base_dir
  puts "An arguments is invalid!"
  exit(1)
end

m = /^(.*)([^\/]|\/)$/.match base_url
if m
  base_url = m[1]
end

Find.find(base_dir) {|path|
  Find.prune if path == './vendor'
  m = /^#{base_dir}\/(.*)\.adoc$/.match path
  if m
    ts = `git --no-pager log --pretty=%at -n1 #{path}`
    if ts.length > 0
      mtime = Time.at(ts.to_i)
      result.push "  <url>\n    <loc>#{base_url}/#{m[1]}.html</loc>\n    <lastmod>#{mtime.strftime("%Y-%m-%d")}</lastmod>\n  </url>"
    else
      result.push "  <url>\n    <loc>#{base_url}/#{m[1]}.html</loc>\n  </url>"
    end
  end
} 

result.push "</urlset>"

puts result.join("\n")