FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/

COPY index.html /var/www/html/index.html
COPY index.html /var/www/html/style.css
COPY index.html /var/www/html/script.js

EXPOSE 80

CMD ["nginx", "g", "daemon off;"]