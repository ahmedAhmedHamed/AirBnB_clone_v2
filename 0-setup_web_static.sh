#!/usr/bin/env bash
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
# chown -R ubuntu:ubuntu /data/
touch /etc/nginx/conf.d/prepare_your_web_servers.conf
echo 'server {
    listen 80;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}' > /etc/nginx/conf.d/prepare_your_web_servers.conf

