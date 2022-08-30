FROM centos:7
RUN yum -y install httpd crul
ENTRYPOINT /usr/sbin/httpd && bash
HEALTHCHECK --interval=2m --timeout=3s CMD curl 127.0.0.1 || exit 1
