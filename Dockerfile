from debian:testing

run sed -e 's/deb.debian.org/debian.mirrors.ovh.net/g' -i /etc/apt/sources.list
run apt-get update \
    && apt-get install -y \
      hugo \
      imagemagick \
      make \
    && apt-get clean

add . /site
workdir /site
run make
cmd /usr/bin/hugo server --port 80 --cleanDestinationDir --destination=/var/www
