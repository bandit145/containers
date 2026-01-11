FROM docker.io/library/python:3.10-trixie
RUN apt update && apt -y install libzmq3-dev
RUN curl https://raw.githubusercontent.com/saltstack/salt/refs/tags/v3006.18/requirements/static/pkg/py3.10/linux.txt -o /tmp/reqs.txt
RUN pip install salt==3006.18
RUN pip install -r /tmp/reqs.txt
RUN mkdir /var/log/salt
RUN mkdir /srv/salt
RUN mkdir /srv/pillar
RUN mkdir /etc/salt
