<?php

class User {

    public $func = "shell_exec";
    public $data = NULL;
    public static function getAllUser() {
        $users = array(array('id' => 1, 'name' => 'kaibro', 'password' => 'easypeasy666'));
        return $users;
    }

    public static function getNameByID($id) {
        $users = User::getAllUser();
        for($i = 0; $i < count($users); $i++) {
            if($users[$i]['id'] === $id) {
                return $users[$i]['name'];
            }
        }
        return NULL;
    }

    public static function getIDByName($name) {
        $users = User::getAllUser();
        for($i = 0; $i < count($users); $i++) {
            if($users[$i]['name'] === $name) {
                return $users[$i]['id'];
            }
        }
        return NULL;
    }

    public static function check($name, $password) {
        $users = User::getAllUser();
        for($i = 0; $i < count($users); $i++) {
            if($users[$i]['name'] === $name && $users[$i]['password'] === $password)
                return true;
        }
        return false;
    }

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

    public static function getFunc() {
        return $this->func;
    }

}
