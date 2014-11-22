require 'rake/docker_lib'
require 'rake/copy_if_obsolete'

output='.target/www'

namespace :pelican do
  desc "Build html for local test"
  task :html do
    sh 'pelican', 'content', '-o', output, '-s', 'pelicanconf.py'
  end

  desc "Build html for publish target"
  task :publish do
    sh 'pelican', 'content', '-o', output, '-s', 'publishconf.py'
  end

  desc "Start pelican development server"
  task :start => "pelican:html" do
    sh "cd #{output} && python -m pelican.server 8000 2>&1 &"
  end 

  task :stop do
    sh "echo 'killall qui va bien à faire'"
  end 
end

Rake::DockerLib.new("deliverous/blog") do
  sh "CGO_ENABLED=0 go build -a --ldflags '-s -extldflags \"-static\"' git.deliverous.com/deliverous/goserve.git/goserve"
end

task :prepare => "pelican:publish"

task :run => [:build, :stop] do
  sh "docker run --name blog -d -p 8000:80 deliverous/blog"
end

task :stop do
  `docker stop blog ; docker rm blog`
end

