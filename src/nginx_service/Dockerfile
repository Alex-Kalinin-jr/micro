FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ./html/* /var/www/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]