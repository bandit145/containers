ARG BASE_CONTAINER=containers.bove.online/base-stream10:latest
FROM ${BASE_CONTAINER}
COPY repos.repo /etc/yum.repos.d/repos.repo
RUN dnf remove -y subscription-manager && dnf install -y epel-release centos-release-hyperscale 
RUN dnf update -y
RUN dnf install --enablerepo=crb -y salt-master
