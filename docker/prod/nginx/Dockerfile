FROM nginx:latest

RUN rm  /etc/nginx/conf.d/default.conf
RUN mkdir -p /nginx_proxy_cache

RUN mkdir -p /etc/nginx/conf.d


#COPY ./docker/nginx/django.proxy /etc/nginx/conf.d
COPY ./docker/prod/nginx/django.conf /etc/nginx/conf.d



