#!/usr/bin/env bash
# Setup both servers
if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update -y
	sudo apt-get install -y nginx
fi
# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# Create a basic HTML
echo "<html><head></head><body>Test Page</body></html>" | sudo tee /data/web_static/releases/test/index.html
# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/
# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
nginx_config="
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}"

echo "$nginx_config" | sudo tee "$config_file" > /dev/null
# Restart Nginx
sudo service nginx restart
