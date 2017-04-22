from tclavier/nginx

run apt-get update \
    && apt-get install -y \
      hugo \
      imagemagick \
      make \
    && apt-get clean

add . /site
workdir /site
run make
run /usr/bin/hugo --destination=/var/www 
add nginx_vhost.conf /etc/nginx/conf.d/blog.conf

