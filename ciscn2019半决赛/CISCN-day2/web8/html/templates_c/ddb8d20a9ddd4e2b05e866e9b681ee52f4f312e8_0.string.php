<?php
/* Smarty version 3.1.30, created on 2019-06-23 10:32:27
  from "ddb8d20a9ddd4e2b05e866e9b681ee52f4f312e8" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f553b89a964_10346678',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f553b89a964_10346678 (Smarty_Internal_Template $_smarty_tpl) {
?>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>A Simple IP Address API</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <div class="row">
        <div style="float:left;">
            <h1>IP</h1>
            <h2 class="hidden-xs hidden-sm">A Simple Public IP Address API</h2>
        </div>
		<div style="float:right;margin-top:30px;">Current IP:172.29.14.163		</div>
    </div>

    <div class="why row">
        <div class="col-xs-12">
            <h2>Why use?</h2>
            <div class="row">
                <div class="col-xs-offset-1 col-xs-10">
                    <p>
                        Do you need to get the public IP address ? Do you have the requirements to obtain the servers’ public IP address? Whatever the reason,sometimes a public IP address API are useful.
                    </p>
                    <p>
                        You should use this because:
                    </p><ul>
                    <li>You can initiate requests without any limit.</li>
                    
                    <li>Does not record the visitor information.</li>
                    
                    </ul>
                    <p></p>
                </div>
            </div>
        </div>
    </div>
    <div class="api row">
        <div class="col-xs-12">
            <h2>API Usage</h2>
            <div class="row">
                <div class="col-xs-offset-1 col-xs-11">
                    
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered table-hover">
                            <thead>
                            <tr>
                                <td>-</td>
                                <td>API URI</td>
                                <td width="50px">Type</td>
                                <td>Sample Output</td>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td>get IP</td>
                                <td><code>http://172.29.14.108/index.phpapi</code></td>
                                <td><code>text/html</code></td>
                                <td><code>8.8.8.8</code></td>
                            </tr>
                            <tr>
                                <td>get XFF(X-Forwarded-For)</td>
                                <td><code>http://172.29.14.108/index.phpxff</code></td>
                                <td><code>text/html</code></td>
                                <td><code>8.8.8.8</code></td>
                            </tr>
                            
                            
                            </tbody>
                        </table>
                    </div>

                    
                </div>
            </div>
        </div>
    </div>
    <div class="examples row">
        
    </div>

    <div class="row">
        <div class="col-xs-12">
            <h2 style="margin-bottom:0;">Connection</h2>
            <div class="row">
                <div class="col-xs-offset-1 col-xs-10">
                    <h3>Request-Header</h3>
                    <pre>GET / HTTP/2.0
Host: www.ip.la
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8
Cache-Control: max-age=0
Dnt: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36

</pre>
                </div>
            </div>
        </div>
    </div>
    <footer>
        <p style="text-align:center;font-size:14px;">Build With Smarty !</p>
    </footer>
</div>

</body></html><?php }
}
