from tclavier/nginx

run apt-get update \
 && apt-get install -y \
    hugo \
    imagemagick \
    make \
    git \
    wget \
 && apt-get clean

run wget https://github.com/spf13/hugo/releases/download/v0.21/hugo_0.21_Linux-64bit.deb -O /tmp/hugo.deb \
 && dpkg -i /tmp/hugo.deb \
 && rm -f /tmp/hugo.deb

add . /site
run rm -rf /site/themes/template-hugo-deliverous
run git clone --depth=1 https://github.com/deliverous/template-hugo-deliverous /site/themes/template-hugo-deliverous
workdir /site
run make
run hugo --destination=/var/www
add nginx_vhost.conf /etc/nginx/conf.d/blog.conf
