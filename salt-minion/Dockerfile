FROM quay.io/centos/centos:stream9
COPY salt.repo /etc/yum.repos.d/salt.repo
RUN dnf install -y epel-release && dnf install -y salt-minion hwinfo systemd systemd-networkd dbus-broker git iproute systemd-resolved python3-dnf-plugin-versionlock openssh-server firewalld centos-release-hyperscale
RUN systemctl enable salt-minion && systemctl enable dbus-broker
RUN echo "ForwardToConsole=yes" >> /etc/systemd/journald.conf
CMD ["/sbin/init"]
