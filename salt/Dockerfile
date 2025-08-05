FROM quay.io/centos/centos:stream9
COPY salt.repo /etc/yum.repos.d/salt.repo
RUN dnf install -y epel-release && dnf install -y salt-master salt-minion salt-cloud salt-api hwinfo systemd systemd-networkd dbus-broker git iproute
RUN systemctl enable salt-minion && systemctl enable salt-master && systemctl enable dbus-broker
RUN echo "ForwardToConsole=yes" >> /etc/systemd/journald.conf
CMD ["/sbin/init"]
