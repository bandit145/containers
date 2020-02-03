FROM alpine:latest

RUN apk update && apk add tftp-hpa alpine-ipxe-undionly_kpxe alpine-ipxe-ipxe_pxe
VOLUME /var/tftpboot/
EXPOSE 69/udp
CMD /usr/sbin/in.tftpd -Lv -s /var/tftpboot