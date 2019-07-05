<html>
<head>
    <meta charset="utf-8">
    <title></title>
    <meta name="keywords" content="">
    <meta name="description" content="">
    <link rel="stylesheet" href="/static/css/css.css" />
    <link rel="stylesheet" href="/static/css/common.min.css" />
    <link rel="stylesheet" href="/static/css/ms-style.min.css" />
    <link rel="stylesheet" href="/static/css/personal_member.min.css" />
    <link rel="stylesheet" href="/static/css/Snaddress.min.css" />
    <link rel="stylesheet" href="/static/css/sui.css" />
    <style>
        body {
            background: #f5f5f5;
        }
        .sui-table th{
            padding: 16px 8px;
            line-height: 18px;
            text-align: center;
            vertical-align: middle;
            border-top: 1px solid #e6e6e6;
            font-weight: normal;
            font-size: 14px;
            color: #333333;
        }
        .sui-table td {
            padding: 16px 8px;
            line-height: 18px;
            text-align: center;
            vertical-align: middle;
            border-top: 1px solid #e6e6e6;
            font-weight: normal;
            font-size: 12px;
            color: #333333;
        }
        img {
            max-width: 100%;
            height: auto;
            /*vertical-align: bottom;*/
            border: 0;
            -ms-interpolation-mode: bicubic;
            margin-left: -10px;
        }
        a{
            color: #000000;
        }
    </style>
</head>

<body class="ms-body">
<header class="ms-header ms-header-inner ms-head-position">
    <article class="ms-header-menu">
        <style type="text/css">
            .nav-manage .list-nav-manage {
                position: absolute;
                padding: 15px 4px 10px 15px;
                left: 0;
                top: -15px;
                width: 90px;
                background: #FFF;
                box-shadow: 1px 1px 2px #e3e3e3, -1px 1px 2px #e3e3e3;
                z-index: 10;
            }

            .ms-nav li {
                float: left;
                position: relative;
                padding: 0 20px;
                height: 44px;
                font: 14px/26px "Microsoft YaHei";
                color: #FFF;
                cursor: pointer;
                z-index: 10;
            }
            .personal-member .main-wrap {
                width: 1068px;
                margin: 15px 0 30px 180px;
                padding: 0 0 39px 0;
                border: 1px solid #ddd;
                background: none;
            }
        </style>
        <div class="header-menu">
            <div class="ms-logo">
                <a class="ms-head-logo"><span style="font-size: 30px;color: #fff;font-weight: bold;    line-height: 28px;;">Hello Cat</span></a>

            </div>
            <nav class="ms-nav">
                <ul>
                    <li class=""><a href="/" style="padding-bottom: 20px;border-bottom: 3px #fff solid;">首页</a><i class="nav-arrow"></i></li>
                    <li class="nav-manage selected">
                        <a href="/userinfo">账户管理</a>
                    </li>
                    {{if .IsAdmin}}
                    <li class="nav-manage selected">
                        <a href="/admin">后台管理</a>
                    </li>
                    {{end}}
                    <li class="nav-manage selected">
                        <a href="/auth/logout">登出</a>
                    </li>
                </ul>
            </nav>
        </div>

    </article>

    <article class="ms-useinfo">
        <div class="header-useinfo" id="">
            <div class="ms-avatar">
                <div class="useinfo-avatar">
                    <img src="{{.Avatar}}">
                </div>
                <a>{{.Username}}</a>
            </div>

            <div class="ms-name-info">
                <div class="link-myinfo">
                    <a>UID:{{.UID}}</a>
                </div>
            </div>
        </div>

    </article>
</header>
<div id="ms-center" class="personal-member">
    <div class="cont-main">
        <div style="border: 0px;">
            <div class="server-wrapper">
                <div class="server-tab" style="margin-top: 26px;">
                    <div style=" float: left;vertical-align: bottom;">
                        <div>
                            <input id="msg" type="text">
                            <button onclick="send()">Submit</button>
                        </div>
                        <div style="width: 1200px;padding:10px;display: inline-block;margin-top: 20px;background-color: #fff;">
                            <div style="border-bottom: 1px #ccc solid;">
                                <p style="font-size: 20px;text-align: left;">消息</p>
                            </div>
                            {{range $index, $message := .Messages}}
                                <div style="padding: 20px 20px;border-bottom: 1px #F5F5F5 solid;height: 150px;">
                                    <div style="float: left;margin-top: 10px;">
                                        <img src="{{$message.Avatar}}" width="150" height="150"/>
                                    </div>
                                    <div style="float: left;margin-top: 20px;">
                                        <p>{{$message.Username}} (UID: {{$message.Uid}})</p>
                                        <p>{{$message.Msg}}</p>
                                    </div>
                                </div>
                            {{end}}
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>
<div class="clear "></div>
<div class="ng-footer ">

			<textarea class="footer-dom " id="footer-dom-02 ">
			</textarea>
    <div class="ng-fix-bar "></div>
</div>
<style type="text/css ">

    .ng-footer {
        height: 130px;
        margin-top: 0;
    }


    .ng-s-footer {
        height: 130px;
        background: none;
        text-align: center;
    }

    .ng-s-footer p.ng-url-list {
        height: 25px;
        line-height: 25px;
    }

    .ng-s-footer p.ng-url-list a {
        color: #666666;
    }

    .ng-s-footer p.ng-url-list a:hover {
        color: #f60;
    }

    .ng-s-footer .ng-authentication {
        float: none;
        margin: 0 auto;
        height: 25px;
        width: 990px;
        margin-top: 5px;
    }

    .ng-s-footer p.ng-copyright {
        float: none;
        width: 100%;
    }

    .root1200 .ng-s-footer p.ng-copyright {
        width: 100%;
    }
</style>
<div style="text-align:center;">
</div>

<script>
    var msg = document.getElementById("msg")
    function send() {
        let request = new XMLHttpRequest()
        let url = ""
        request.open("post", url, true)
        let data = new FormData()
        data.append("msg", msg.value)
        request.onreadystatechange = function() {
            if (this.readyState == 4) {
                if (this.responseText == "success")
                    window.location.reload()
            }
        }
        request.send(data)
    }
</script>

</body>
</html>