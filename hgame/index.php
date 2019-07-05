<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="./layout.css" media="screen">
        <meta charset="utf-8">
        <title>HappyXss</title>
    </head>
    <body>
        <div class="title">
            <h1>HappyXss</h1>           
            <hr>
        </div>
        <div class="message">
            <div class="input">
                <form class="form" action="" method="post">
                    <textarea type="text" name="payload"></textarea><br>
                    <button type="submit">测试</button>
                </form>
                <br>
            </div>
            <div>
                <div>
                    <form action="" method="post">
                        code value: <input type="text" name="code">
                        <input type="submit" name="submit" value="上交">
                    </form>

                </div>
                <div>
                    <?php
                        session_start();
                        error_reporting(0);
                        header("Content-Security-Policy: default-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src * ");
                        header('X-XSS-Protection: 0');

                        if(!isset($_SESSION["code"])){     
                            $_SESSION["code"]=substr(md5(mt_rand()),0,4);  
                        }else{
                            if(isset($_POST["code"])){ 
                                if(substr(md5($_POST["code"]),0,4)!==$_SESSION["code"]){         
                                    echo 'substr(md5($_POST["code"]),0,4)==='.$_SESSION['code'].'<br>';   
                                    die("wrong code.....");
                                }else{
                                    $_SESSION["code"]=substr(md5(mt_rand()),0,4);  
                                    echo 'right code <br>';
                                }
                            }
                            echo 'substr(md5($_POST["code"]),0,4)==='.$_SESSION['code'].'<br>';  
                        }

                        if(isset($_POST["payload"])){
                            $payload=$_POST["payload"];
                            $black_str = "/(xml)|(document)|(cookie)|(img)|(svg)|(window)|(location)|(href)|(<script>)|(<\/script>)|(meta)|(link)|(onerror)|(onload)|&|#|\"/i";
                            $txt=" Happy! ";
                            $payload = preg_replace($black_str,$txt,$payload);
                            echo $payload;
                            $_SESSION['payload'] = $payload;
                        }

                        session_write_close();
                        if (isset($_POST['submit'])) {
                            $sess_id = session_id();
                            $sess_id = str_replace(PHP_EOL, '', $sess_id);
                            $cmd = "../bot -u http://127.0.0.1 -a User-Agent=FlowerFox -c PHPSESSID=$sess_id\&Flag=hgame{Xss_1s_Re@llY_Haaaaaappy!!!}";
                            shell_exec($cmd);
                            echo "<script>alert('消息已查看')</script>";
                            die();
                        }
                    ?>
                </div>
            </div>
        </div>
    </body>
</html>

