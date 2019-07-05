<?php
echo '<div align="center"><font size=6>卫星控制系统</font></div>';
echo'
<form action="checkyou.php" method="post">
        <fieldset>
            <legend>员工请登录</legend>
            <ul>
                <li>
                    <label>用户名/工号:</label>
                    <input type="text" name="user">
                </li>
                <li>
                    <label>密   码:</label>
                    <input type="password" name="passwd">
                </li>
                <li>
                    <label> </label>
                    <input type="checkbox" name="remember" value="yes">0.1天内自动登录
                </li>
                <li>
                    <label> </label>
                    <input type="submit" name="login" value="登录">
                </li>
            </ul>
        </fieldset>
    </form>
'
?>

<script type="text/javascript">
         window.onload = function() {
             document.onkeydown = function() {
                 var e = window.event || arguments[0];//banF12
                 if(e.keyCode == 123) {
                     return false;//banCtrl+Shift+I
                 } else if((e.ctrlKey) && (e.shiftKey) && (e.keyCode == 73)) {
                     return false;//banShift+F10
                 } else if((e.shiftKey) && (e.keyCode == 121)){
                     return false;
                 }
             };//banrightclick
             document.oncontextmenu = function() {
                 return false;
             }
         }
 </script>