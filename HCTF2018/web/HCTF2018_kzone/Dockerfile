FROM mattrayner/lamp:latest-1604

COPY hctf.sql /home/hctf.sql
COPY init.sh /home/init.sh
COPY apache2.conf /etc/apache2/apache2.conf

RUN echo " <VirtualHost *:80> \n \
    DocumentRoot /var/www/html\n \
    <Directory /var/www/html>\n \
    	Options FollowSymLinks\n \
        Order deny,allow\n \
        AllowOverride None\n  \
        Allow from all\n \
    </Directory>\n \
 </VirtualHost> " > /etc/apache2/sites-available/000-default.conf
RUN rm -rf /var/www/php* && \
	mysql -uroot -e"use mysql;update user set authentication_string=password('root') where user='root';create user 'r00t'@'localhost'identified by 'Fish_k0u_z0ne'; flush privileges;"

EXPOSE 80
