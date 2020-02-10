FROM alpine:latest

RUN apk add bind

RUN mkdir /etc/named_conf/ cp /etc/named.conf.recursive /etc/named_conf/named.conf
VOLUME /etc/named_conf
EXPOSE 53/udp
EXPOSE 53/tcp
CMD /usr/sbin/named -g -c /etc/named_conf/named.conf