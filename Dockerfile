FROM deliverous/wheezy
MAINTAINER olivier.albiez@deliverous.com
MAINTAINER thomas.clavier@deliverous.com

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y --no-install-recommends -q nginx && apt-get clean

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
ADD docker/site.nginx /etc/nginx/sites-enabled/blog

ADD output/ /var/www/

EXPOSE 80

CMD ["/usr/sbin/nginx"]
