FROM scratch
MAINTAINER docker@deliverous.com

ADD goserve /usr/sbin/goserve
ADD www/ /var/www/

EXPOSE 80

CMD ["/usr/sbin/goserve", "-port", "80", "-root", "/var/www"]
