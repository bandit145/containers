FROM alpine:latest

RUN apk update && apk upgrade
RUN mkdir /hi
VOLUME /hi
EXPOSE 67/udp
CMD tail -f /dev/null
