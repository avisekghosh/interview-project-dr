FROM nginx:1.17.6

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx_config/m1.conf /etc/nginx/conf.d/m1.conf
COPY ./nginx_config/m2.conf /etc/nginx/conf.d/m2.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
