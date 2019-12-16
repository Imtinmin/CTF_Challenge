FROM phusion/baseimage

RUN sed -i "s/security.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && sed -i "s/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list

RUN apt-get update && apt-get install php7.2 php7.2-zip php7.2-mysql git vim mysql-server php7.2-curl libapache2-mod-php apache2

COPY ./ctf /var/www/html/www
COPY ctf.sql /

