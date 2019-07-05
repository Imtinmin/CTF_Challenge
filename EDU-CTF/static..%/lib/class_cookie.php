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
