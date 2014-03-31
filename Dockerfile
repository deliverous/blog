FROM wheezy
MAINTAINER olivier.albiez@deliverous.com
MAINTAINER thomas.clavier@deliverous.com

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install --assume-yes --no-install-recommends -q nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD output/ /var/www/

EXPOSE 80

CMD ["/usr/sbin/nginx"]
