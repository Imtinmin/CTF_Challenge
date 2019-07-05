<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="#" />
    <link type="text/css" rel="styleSheet"  href="static/css/main.css" />
    <link type="text/css" rel="styleSheet"  href="static/css/form.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>账号登录</title>
</head>


<body>
<div id="bg">
    <div id="hint"><!-- 提示框 -->
        <p>登录失败</p>
    </div>
    <div id="login_wrap">
        <div id="login"><!-- 登录注册切换动画 -->
            <div id="status">
                <i style="top: 0">Log</i>
                <i style="top: 35px">Sign</i>
                <i style="right: 5px">in</i>
            </div>
            <span>
                    <form action="post">
                        <p class="form"><input type="text" id="user" placeholder="username"></p>
                        <p class="form"><input type="password" id="passwd" placeholder="password"></p>
                        <p class="form confirm"><input type="password" id="confirm-passwd" placeholder="confirm password"></p>
                        <input type="button" value="Log in" class="btn" onclick="login()" style="margin-right: 20px;">
                        <input type="button" value="Sign in" class="btn" onclick='signin()' id="btn">
                    </form>
                    <a href="#">Forget your password?</a>
                </span>
        </div>

        <div id="login_img"><!-- 图片绘制框 -->
            <span class="circle">
                    <span></span>
                    <span></span>
                </span>
            <span class="star">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </span>
            <span class="fly_star">
                    <span></span>
                    <span></span>
                </span>
            <p id="title">CLOUD</p>
        </div>
    </div>
</div>
</body>
<script src="/static/js/form.js"></script>
</html>
