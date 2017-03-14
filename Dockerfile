from debian:testing

run apt-get update && apt-get install -y \
      make \
      hugo \
 && apt-get clean

add . /site
workdir /site
run make
cmd /usr/bin/hugo server --port 80 --cleanDestinationDir --destination=/var/www
