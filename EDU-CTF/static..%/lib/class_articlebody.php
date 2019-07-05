<?php

class ArticleBody {
    public $title;
    public $content;

    function __construct($title, $content) {
        $this->title = $title;
        $this->content = $content;
    }

    function update($title, $content) {
        $this->title = $title;
        $this->content = $content;
    }

    function __toString() {
        $str = '';
        $str .= "<h2 style='color:#63ff00'>" . htmlentities($this->title) . "</h2>";
        $str .= "<p>" . htmlentities($this->content) . "</p>";
        return $str;
    }

    function __destruct() {
        unset($this->title);
        unset($this->content);
    }

}
