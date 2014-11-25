require 'rake/docker_lib'
require 'rake/compile_go'

output='.target/www'

namespace :pelican do
  desc "Build html for local test"
  task :html do
    sh 'pelican', 'content', '-o', output, '-s', 'pelicanconf.py', '--cache-path', '.target/cache'
  end

  desc "Build html for publish target"
  task :publish do
    sh 'pelican', 'content', '-o', output, '-s', 'publishconf.py', '--cache-path', '.target/cache'
  end

  desc "Start pelican development server"
  task :start => "pelican:html" do
    sh "cd #{output} && python -m pelican.server 8000 2>&1 &"
  end 

  desc "Stop pelican development server"
  task :stop do
    sh "echo 'killall qui va bien à faire'"
  end 
end

namespace :docker do
  Rake::DockerLib.new("deliverous/blog") do
    prepare do
      Go::compile(repository: 'git.deliverous.com/deliverous/goserve.git', 
            package: 'git.deliverous.com/deliverous/goserve.git/goserve', 
            tag: EtcdVersion, 
            workspace: "#{Dir.pwd}/go",
            goversion: "1.3.3",
            target: "#{Dir.pwd}",
            static: true,
            strip: true)
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
