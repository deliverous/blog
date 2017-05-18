from tclavier/nginx
run apt-get update \
    && apt-get install -y \
      git \
      hugo \
      imagemagick \
      make \
    && apt-get clean
add . /site
run rm -rf /site/themes/template-hugo-deliverous
run git clone https://github.com/deliverous/template-hugo-deliverous /site/themes/template-hugo-deliverous
workdir /site
run make
run /usr/bin/hugo --destination=/var/www 
add nginx_vhost.conf /etc/nginx/conf.d/blog.conf
