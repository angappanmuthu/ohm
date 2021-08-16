FROM nginx:latest

# RUN rm /etc/nginx/conf.d/django.conf
RUN rm -f -- /etc/nginx/conf.d/default.conf
RUN mkdir -p /nginx_proxy_cache

#COPY ./docker/nginx/django.proxy /etc/nginx/conf.d
COPY ./docker/prod/nginx/default.conf /etc/nginx/conf.d



