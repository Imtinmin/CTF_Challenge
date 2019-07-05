<?php
class OldFileManager {

    public $name = '';
    public $content = '';
    public $mode = '';

    function __construct($m, $f, $c=null) {
        $this->mode = $m;
        $this->name = $f;
        $this->content = $c;
    }

    function __destruct() {
        if( $this->mode === "delete" )
            $this->delFile();
        if( $this->mode === "upload" )
            file_put_contents($this->name, $this->content);
    }

    function getFile() {
        if( $this->mode === "read" )
            return file_get_contents($this->name);
        else
            return "Bye";
    }

    function modifyFile() {
        if( $this->mode === "modify" )
            file_put_contents($this->name, $this->content);
    }

    function delFile() {
        unlink($this->name);
    }

}
