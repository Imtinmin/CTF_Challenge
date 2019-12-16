<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Login</title>
    <link href="favicon.ico" rel="shortcut icon" />
    <link href="https://cdn.bootcss.com/twitter-bootstrap/3.4.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<script src="static/js/login.js"></script>

<div class="modal-dialog" style="margin-top: 10%;">
    <div class="modal-content">
        <div class="modal-header">

            <h4 class="modal-title text-center" id="myModalLabel">登录</h4>
        </div>
        <div class="modal-body" id = "model-body">
            <div class="form-group">

                <input type="text" class="form-control"placeholder="用户名" autocomplete="off" id="username">
            </div>
            <div class="form-group">

                <input type="password" class="form-control" placeholder="密码" autocomplete="off" id="password">
            </div>
        </div>
        <div class="modal-footer">
            <div class="form-group">
                <button type="button" class="btn btn-primary form-control" onclick="loginAjax()">登录</button>
            </div>
            <div class="form-group">
                <button type="button" class="btn btn-default form-control" onclick="checkResiger()">注册</button>
            </div>

        </div>
    </div><!-- /.modal-content -->
</div><!-- /.modal -->

</body>
</html>