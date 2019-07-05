<?php

class Article {
    public $author; // user id
    public $date;
    public $body;

    function __construct($title, $content) {
        $this->author = $_SESSION['user'];
        $this->body = new ArticleBody($title, $content);
    }

    function setBody($title, $content) {
        if(is_a($this->body, "ArticleBody")) {
            $this->body->update($title, $content);
        } else {
            $this->body = new ArticleBody($title, $content);
        }
    }

    function __destruct() {
        if(isset($body)) {
            unset($body);
        }
    }

    function __toString() {
        $str = '';
        $str .= $this->body;
        return $str;
    }

    function save() {
        $ok = false;
        for($i = 1; $i <= 2500; $i++) {
            $f = "/var/www/app/articles/" . $i . ".txt";
            if(!file_exists($f)) {
                file_put_contents($f, $this->__toString());
                $ok = true;
                break;
            }
        }

        // fxxk! too many articles
        if(!$ok) {
            exec("rm /var/www/app/articles/*.txt");
            die("Saving error!");
        }
    }

    public static function getAll() {
        $res = '';
        $first = false;
        for($i = 1; $i <= 2500; $i++) {
            $f = "/var/www/app/articles/" . $i . ".txt";
            if(file_exists($f)) {
                $c = file_get_contents($f);
                if(!$first) {
                    $res .= $c;
                    $first = !$first;
                } else {
                    $res .= "<hr>";
                    $res .= $c;
                }
            }
        }
        return $res;
    }

}