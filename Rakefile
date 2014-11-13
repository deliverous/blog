require 'rake/docker_lib'
require 'rake/copy_if_obsolete'


Rake::DockerLib.new("registry.deliverous.net/deliverous/blog") do
  sh 'pelican', '../content', '-o', 'www', '-s', '../pelicanconf.py'  
  sh "CGO_ENABLED=0 go build -a --ldflags '-s -extldflags \"-static\"' git.deliverous.com/deliverous/goserve.git/goserve"
end
