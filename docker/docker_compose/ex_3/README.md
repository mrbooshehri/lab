1. Create a network nextcloud_network
1. In an empty directory create docker-compose.yaml
1. You compose should contain	four services
	1. Nginx reverse proxy(service name: proxy)
	1. Let's encrypt(service name: letsencrypt)
	1. MariaDB(service name: db)
	1. nextcloud(service name: app)

# Proxy info

1. image jwildr/nginx-proxy:alpine
1. container_name:nextcloud-porxy
1. connect the container to nextcloud-network
1. publish port 80 and 443
1. define the following volumes
	1. - ./proxy/conf.d:/etc/nginx/conf.d:rw
	1. - ./proxy/vhost.d:/etc/nginx/vhost.d:rw
	1. - ./proxy/html:/urs/share/nginx/html:rw
	1. - ./proxy/certs:/etc/nginx/certs:ro
	1. - ./proxy/localtime:/etc/localtime:ro
1. set restart policy to unless-stop

# Letsencryps info

1. image: jrcs/letsencrpt-nginx-proxy-companion
1. container_name:nextcloud-letsencrypt
1. connect the container to nextcloud-network
1. depends_on: proxy
1. define the following volumes
	1. - ./proxy/vhost.d:/etc/nginx/vhost.d:rw
	1. - ./proxy/html:/urs/share/nginx/html:rw
	1. - ./proxy/certs:/etc/nginx/certs:ro
	1. - ./proxy/localtime:/etc/localtime:ro
	1. - /var/run/docker.sock:/var/run/docker.sock:ro
1. set restart policy to unless-stop

# MarioDB info 

1. image: mariadb
1. container_name:nextcloud-mariadb
1. connect the container to nextcloud-network
1. define the following envs
	1. MYSQL_ROOT_PASSWORD=123
	1. MYSQL_PASSWORD=456
	1. MYSQL_DATABASE=nextcloud
	1. MYSQL_USER=nextcloud
1. set restart policy to unless-stop

# Nextcloud info

1. image: nextcloud:latest
1. container_name:nextcloud-app
1. connect the container to nextcloud-network
1. depends_on: proxy, db, letsencrypt
1. define the following volumes
	1. -./app/config:/vat/www/html/config
	1. -./app/custom_app:/var/www/html/custom_app
	1. -./app/data:/var/www/html/data
	1. -./app/themes:/var/www/html/themes
	1. -/etc/localtime:/etc/localtime:ro
1. define the following envs
	1. - VIRTUAL_HOST=nextcloud.yourdomain/your machine ip docker hsot
	1. - LETSENCRYPT_HOST=nextcloud.yourdomain/your machine ip docker hsot
	1. - LETSENCRYPT_EMAIL=your email
1. set restart policy to unless-stop


# other top levels

volumes:
	nextcloud:
	db:
network:
	nextcloud-network
