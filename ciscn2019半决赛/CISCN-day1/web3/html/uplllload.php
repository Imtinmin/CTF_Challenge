<?php
error_reporting(0);
if (isset($_FILES["file"])) {
    $filename = $_FILES["file"]["name"];
    $arr = explode('.', $filename);
    $ext = end($arr);
    if($ext === 'gif'){
    $ext = '.gif';

    $dst = $_FILES["file"]["name"] . $ext;
    move_uploaded_file($_FILES["file"]["tmp_name"], $dst);
    echo "文件保存位置: {$dst}<br />";
}else{
    die('only .gif is allowed!');
}
}
?>
<html>

<head>
    <meta charset="UTF-8">
</head>

<body>

    <form method="post" enctype="multipart/form-data">
        <label for="file">file:</label>
        <input type="file" name="file" id="file" />
        <br />
        <input type="submit" name="submit" value="Submit" />
    </form>

</body>

</html>