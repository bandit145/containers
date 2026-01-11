FROM quay.io/centos-bootc/centos-bootc:stream10
COPY repos.repo /etc/yum.repos.d/repos.repo
RUN touch /etc/ostree/prepare-root.conf
RUN dnf remove -y subscription-manager && dnf install -y epel-release centos-release-hyperscale 
RUN dnf update -y
RUN dnf install --enablerepo=crb -y htop \
procps-ng \
sysstat \
tcpdump \
conntrack-tools \
bcc-tools \
systemd-resolved \
screen \
tmux \
nano \
grub2-efi-x64-modules \
vim-enhanced \
libsemanage \
python3-dnf-plugin-versionlock \
python3-setools \
python3-dns \
salt-minion \
kernel-headers \
kernel-devel \
policycoreutils-python-utils firewalld && dnf clean all && systemctl enable salt-minion
RUN dnf clean all
