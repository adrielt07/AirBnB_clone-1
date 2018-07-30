#!/usr/bin/env bash
# Sets up web servers for the deployment of webstatic
if [ ! -f "/usr/sbin/nginx" ]; then
    sudo apt-get -y install nginx
fi

if [ ! -d "/data/web_static/releases/test" ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi

if [ ! -d "/data/web_static/shared/" ]; then
    sudo mkdir -p /data/web_static/shared/
fi

if [ ! -d "/data/web_static/current" ]; then
    sudo ln -sf /data/web_static/releases/test /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/

if [ ! -f "/data/web_static/releases/test/index.html" ]; then
    echo "Hello Holberton: This is a test" >> /data/web_static/releases/test/index.html
fi
line_search="404.html;"
alias_line="location /hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}"
sudo sed -i "/$line_search/ a\ $alias_line" /etc/nginx/sites-enabled/default
sudo service nginx restart
