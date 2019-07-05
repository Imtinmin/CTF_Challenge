#!/bin/bash
service mysql start;

mysql -uroot -e"use mysql;update user set authentication_string=password('@hctf_k0u_z0ne') where user='root';create user 'r00t'@'localhost'identified by 'Fish_k0u_z0ne'; flush privileges;"
mysql -uroot -p\@hctf_k0u_z0ne -e"create database hctf_kouzone;grant select,insert on hctf_kouzone.* to 'r00t'@'localhost';grant select on mysql.* to 'r00t'@'localhost';flush privileges;"

mysql -uroot -p\@hctf_k0u_z0ne hctf_kouzone < /home/hctf.sql
a2enmod remoteip
service apache2 restart
