<?php
if (!defined('LFI')) {
    echo "Include me!";
    exit();
}

if (isset($_FILES["file"])) {
    $filename = $_FILES["file"]["name"];
    $fileext = ".gif";
    switch ($_FILES["file"]["type"]) {
        case 'image/gif':
            $fileext = ".gif";
            break;
        case 'image/jpeg':
            $fileext = ".jpg";
            break;
        default:
            echo "Only gif/jpg allowed";
            exit();
    }
    $dst = "upload/" . $_FILES["file"]["name"] . $fileext;
    move_uploaded_file($_FILES["file"]["tmp_name"], $dst);
    echo "文件保存位置: {$dst}<br />";
}
?>
<html>

<head>
    <meta charset="UTF-8">
</head>

<body>
    我们不能让选手轻而易举的搜索到上传接口。<br />
    即便是运气好的人碰巧遇到了，我相信我们的过滤是万无一失的(才怪
    <form method="post" enctype="multipart/form-data">
        <label for="file">来选择你的文件吧:</label>
        <input type="file" name="file" id="file" />
        <br />
        <input type="submit" name="submit" value="Submit" />
    </form>

</body>

</html>