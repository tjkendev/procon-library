# the script for generating sitemap.xml
require 'find'
require 'fileutils'

base_url = ARGV[0]
base_dir = ARGV[1]
dest_dir = ARGV[2]

if !base_url || !base_dir || !dest_dir
  puts "An arguments is invalid!"
  exit(1)
end

m = /^(.*)([^\/]|\/)$/.match base_url
if m
  base_url = m[1]
end

def generate_sitemap_text base_url, base_dir
  result = ["<?xml version='1.0' encoding='UTF-8' ?>
  <urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"]

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
  result.join("\n")
end

def generate_robots_text base_url
  result = ["User-agent: *"]
  result.push "Sitemap: #{base_url}/sitemap.xml"

  result.join("\n")
end

sitemap_text = generate_sitemap_text base_url, base_dir

File.open("#{dest_dir}/sitemap.xml", "w") do |f|
  f.puts sitemap_text
end

robots_text = generate_robots_text base_url
File.open("#{dest_dir}/robots.text", "w") do |f|
  f.puts robots_text
end