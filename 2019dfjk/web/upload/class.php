<?php

class Show
{
    public $source;
    public $str;
    /*public function __construct($file)
    {
        $text= $this->source;
        $text = base64_encode(file_get_contents($text));
        return $text;
    }*/	本地复现注释掉不会不然打不成
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
    public function __construct()
    {
        $this->params = array();
    }
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
    public function __construct($name)
    {
        $this->str = new Show('index.php');
        $this->str->source = $this->test;

    }
    public function __destruct()
    {
        $this->str->_show();
    }
}
?>
