1. create an empty project called my_wordpress
1. create a docker-compose.yaml
1. define to services
	1. db
	1. wordpress
1. config db as follow
	1. image: mysql:5.7
	1. -db_data:/var/lib/mysql
	1. restart policy: always
	1. set MYSQL_ROOT_PASSWORD, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE
1. config wordpress as follow
	1. image: wordpress:latest
	1. depend_on:db
	1. publish port 8000:80
	1. restart policy: unless_stop
	1. set WORDPRESS_HOST, WORDPRESS_DB_USER, WORDPRESS_PASSWORD, WORDPRESS_DB_NAME
	1. volume db_data: {}
