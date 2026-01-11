FROM docker.io/python:3.10-trixie
ENV SALT_VERSION=3006.18
RUN apt update && apt install -y libzmq3-dev
RUN curl https://raw.githubusercontent.com/saltstack/salt/refs/tags/v${SALT_VERSION}/requirements/static/pkg/py3.10/linux.txt -o /tmp/reqs.txt
RUN pip install salt==${SALT_VERSION}
RUN pip install -r /tmp/reqs.txt

FROM docker.io/python:3.10-slim-trixie
COPY --from=0 /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=0 /usr/local/bin/* /usr/local/bin/

RUN mkdir /var/log/salt && mkdir /etc/salt && mkdir /srv/salt
CMD ["/usr/local/bin/salt-master", "-l", "info"]
