FROM alpine:latest

RUN apk add apache2
VOLUME /var/www/localhost/htdocs
EXPOSE 80/tcp
CMD /usr/sbin/httpd -DFOREGROUND