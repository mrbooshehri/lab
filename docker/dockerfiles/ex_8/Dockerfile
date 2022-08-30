FROM centos:7
RUN yum -y install httpd
EXPOSE 80
VOLUME /var/www/html
ENTRYPOINT /usr/sbin/httpd && /bin/bash
