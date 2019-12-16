create user 'ctf'@''localhost' IDENTIFIED BY ‘swpuctf2019';use mysql;update user set plugin='my_native_password' where User='root';flush privileges;
