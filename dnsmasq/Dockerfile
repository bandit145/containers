FROM alpine:latest

RUN apk add dnsmasq
RUN mkdir /etc/dnsmasq/
RUN cp /etc/dnsmasq.conf /etc/dnsmasq/dnsmasq.conf
VOLUME /etc/dnsmasq/
EXPOSE 67/udp 53/udp 69/udp
CMD /usr/sbin/dnsmasq -d --conf-file=/etc/dnsmasq/dnsmasq.conf