1. create an image based on centos:latest
1. install httpd and curl inside the image
1. add healthcheck to your image as following
	1. HEALTHCHECK --interval=2m --timeout=3s CMD curl 127.0.0.1 || exit 1
1. add entrypoit as follow
	1. ENTRYPOINT /usr/sbin/httpd
1. build the image and check inspect
1. chage the ENTRYPOINT as follow
	1. ENTRYPOINT /usr/sbin/httpd && bash
