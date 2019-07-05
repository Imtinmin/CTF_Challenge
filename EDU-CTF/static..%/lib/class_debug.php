<?php 
// for debug

class Debug {

    public $msg='';

    function __construct($msg = '') {
        $this->msg = $msg;
        $this->fm = new FileManager($this->msg);
    }

    function __toString() {
        $str = "[DEUBG]" . $msg;
        $this->fm->save(); 
        return $str;
    }

    function __destruct() {
        unset($this->msg);
    }
}
