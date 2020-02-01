FROM alpine:latest

RUN apk add nsd
RUN mkdir /run/kea && mv /etc/nsd/nsd.conf.sample /etc/nsd/nsd.conf 
VOLUME /etc/nsd
EXPOSE 53/udp
EXPOSE 53/tcp
CMD /usr/sbin/nsd -c /etc/nsd/nsd.conf -d