FROM alpine:latest

RUN apk add kea
RUN mkdir /run/kea
VOLUME /etc/kea/
EXPOSE 67/udp
CMD /usr/sbin/kea-dhcp4 -c /etc/kea/kea-dhcp4.conf