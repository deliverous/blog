require 'rake/docker_lib'
require 'rake/copy_if_obsolete'


task :pelican_html do
  sh 'pelican', 'content', '-o', '.target/www', '-s', 'pelicanconf.py'
end

task :pelican_publish do
  sh 'pelican', 'content', '-o', '.target/www', '-s', 'publishconf.py'
end

Rake::DockerLib.new("deliverous/blog") do
  sh "CGO_ENABLED=0 go build -a --ldflags '-s -extldflags \"-static\"' git.deliverous.com/deliverous/goserve.git/goserve"
end

task :prepare => :pelican_publish

task :run => [:build, :stop] do
  sh "docker run --name blog -d -p 8000:80 deliverous/blog"
end

task :stop do
  `docker stop blog ; docker rm blog`
end
