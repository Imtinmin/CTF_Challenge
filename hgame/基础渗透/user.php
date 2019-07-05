 
 <?php
require_once('functions.php');
if (!isset($_SESSION['login'])) {
    Header("Location: /login.php");
    exit();
} else {
    echo "<div id='user-info' class='am-container'>";
    echo "<div class='am-form'>";
    echo "<div class='am-form-group am-form-file' id='form-file'>";
    $image = get_avatar($_SESSION['user_id']);
    if ($image != null) {
        echo "<img type='button' src=data:image/png;base64," . $image['content'] . " class='am-circle' id='avatar'>";
    } else {
        echo "<div class='am-circle avatar-tmp' id='avatar'>" . md5($_SESSION['user']) . "</div>";
    }

}

?>

    <input type="file" id="upfile" onchange="SelectImage()">
    </div>
    <button id="upload" class="am-btn am-btn-primary am-disabled">保 存 头 像</button>
    </div>

<?php
echo "<div class='user'><strong>用户名： </strong> " . $_SESSION['user'] . "</div>";
echo "<hr>";
echo "<div class='am-form am-form-horizontal'>";
echo "<strong>原密码：</strong> <input id='oldpassword' type='password'> ";
echo "<br>";
echo "<strong>新密码：</strong> <input id='newpassword' type='password'>";
echo "<br>";
echo "<strong>新密码确认：</strong> <input id='newpassword_again' type='password'> ";
echo "<br>";
echo "</div>";
echo "<button onclick='NewPassword()' class='am-btn am-btn-danger'>确 认 修 改</button>";
echo "</div>";
echo "</div>";
echo "</div>";

echo "<script src='/js/user.js'></script>";
?>