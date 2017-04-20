from tclavier/nginx
MAINTAINER docker@deliverous.com
run apt-get update \
    && apt-get install -y \
      pelican \
      locales \
    && apt-get clean

# Setup locale
run echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen \
    && locale-gen

add nginx_vhost.conf /etc/nginx/conf.d/blog.conf
add . /site
workdir /site
run pelican content -o /var/www -s publishconf.py

