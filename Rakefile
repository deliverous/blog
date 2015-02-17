require 'rake/docker_lib'
require 'rake/compile_go'

output='.target/www'

def pelican_generate(configuration, options={})
  command = "pelican content -o .target/www -s #{configuration} --cache-path .target/cache"
  command += " --debug --autoreload 2>&1 &" if options.has_key? :autoreload 
  sh command
end

namespace :pelican do
  desc "Build html for local test"
  task :html do
    pelican_generate 'pelicanconf.py' 
  end

  desc "Build html for publish target"
  task :publish do
    pelican_generate 'publishconf.py' 
  end

  desc "Start pelican development server"
  task :start do
    pelican_generate 'publishconf.py', autoreload: true
    sh "cd #{output} && python -m pelican.server 8000 2>&1 &"
  end

  desc "Stop pelican development server"
  task :stop do
    sh "pkill -f pelican.server"
  end
end

namespace :docker do
  Rake::DockerLib.new("deliverous/blog") do
    prepare do
      Go::compilation(workspace: "#{Dir.pwd}/go", goversion: "1.3.3") do
          package 'github.com/deliverous/goserve/goserve'
          build 'github.com/deliverous/goserve/goserve', static: true
          strip_binaries
          copy_to Dir.pwd
      end
    end
  end

  task :prepare => "pelican:publish"

  task :run => ['docker:build', 'docker:stop'] do
    sh "docker run --name blog -d -p 8000:80 deliverous/blog"
  end

  task :stop do
    `docker stop blog ; docker rm blog`
  end
end
