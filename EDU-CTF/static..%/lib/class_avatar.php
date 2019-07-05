<?php

class Avatar {
    public $url;

    public static function check() {
        if(isset($_COOKIE['av'])) {
            return true;
        }
        return false;
    }

    public function setAV($u) {
        $this->url = $u;
    }

    public function save() {
        setcookie("av", $this->url);
    }

    public function setAVFromCookie() {
        if(isset($_COOKIE['av'])) {
            $this->setAV($_COOKIE['av']);
        }
        return $this->toString();
    }

    public static function destruct() {
        unset($_COOKIE['av']);
    }

    public function toString() {
        return $this->url;
    }

}

