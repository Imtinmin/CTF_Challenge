<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>about</title>
    <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
    <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        .fakeimg {
            height: 200px;
            background: #aaa;
        }
    </style>
</head>
<body>
<div class="jumbotron text-center" style="margin-bottom:0">
    <h1>WELCOME TO SWPUCTF2019</h1>
</div>

<nav class="navbar navbar-inverse">
    <div class="container-fluid">
    </div>
</nav>
<div class="container">
    <div class="row">
        <div class="col-sm-4">
            <h2>关于我</h2>
            <h5>我的照片:</h5>
            <div class="fakeimg"><?php
                if(!isset($img_file)) {
                    $img_file = '/../favicon.ico';
                }
                $img_dir = dirname(__FILE__) . $img_file;
                $img_base64 = imgToBase64($img_dir);
                echo '<img src="' . $img_base64 . '">';       //图片形式展示
                ?></div>
        </div>
    </div>
</div>

</body>
</html>
<?php
function imgToBase64($img_file) {

    $img_base64 = '';
    if (file_exists($img_file)) {
        $app_img_file = $img_file; // 图片路径
        $img_info = getimagesize($app_img_file); // 取得图片的大小，类型等

        $fp = fopen($app_img_file, "r"); // 图片是否可读权限

        if ($fp) {
            $filesize = filesize($app_img_file);
            $content = fread($fp, $filesize);
            $file_content = chunk_split(base64_encode($content)); // base64编码
            switch ($img_info[2]) {           //判读图片类型
                case 1: $img_type = "gif";
                    break;
                case 2: $img_type = "jpg";
                    break;
                case 3: $img_type = "png";
                    break;
            }

            $img_base64 = 'data:image/' . $img_type . ';base64,' . $file_content;//合成图片的base64编码

        }
        fclose($fp);
    }

    return $img_base64; //返回图片的base64
}
?>
