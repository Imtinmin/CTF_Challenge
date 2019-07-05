<?php

class FileManager {
    private $filename;
    private $content;
    
    function __construct($content) {
        $this->filename = "/var/www/app/articles/error";
        $this->content = $content;
    }

    function save() {
        file_put_contents($this->filename.".log", $this->content);
    }

    function test() {
        shell_exec("ls /");
    }

}
