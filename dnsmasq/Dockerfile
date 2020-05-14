FROM alpine:latest

RUN apk add dnsmasq
RUN mkdir /var/tftp/
VOLUME /etc/dnsmasq.d/
VOLUME /var/tftp/
EXPOSE 67/udp 53/udp 69/udp
CMD /usr/sbin/dnsmasq -d