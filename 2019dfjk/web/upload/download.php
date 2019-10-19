<html>
<pre>

$name = $_GET['name'];
$url = $_SERVER['QUERY_STRING'];
if (isset($name)){
    if (preg_match('/\.|etc|var|tmp|usr/i', $url)){
        echo("hacker!");
    }
    else{
        if (preg_match('/base|class|file|function|index|upload_file/i', $name)){
            echo ("hacker!");
        }
        else{
            $name = safe_replace($name);
            if (preg_match('/base|class|file|function|index|upload_file/i', $name)){
                $filename = $name.'.php';
                $dir ="./";
                $down_host = $_SERVER['HTTP_HOST'].'/';
                if(file_exists(__DIR__.'/'.$dir.$filename)){
                    $file = fopen ( $dir.$filename, "rb" );
                    Header ( "Content-type: application/octet-stream" );
                    Header ( "Accept-Ranges: bytes" );
                    Header ( "Accept-Length: " . filesize ( $dir.$filename ) );
                    Header ( "Content-Disposition: attachment; filename=" . $filename );
                    echo fread ( $file, filesize ( $dir . $filename ) );
                    fclose ( $file );
                    exit ();
                }else{
                    echo ("file doesn't exist.");
                }
            }
            if (preg_match('/flag/i', $name)){
                echo ("hacker!");
            }
        }
    }
}
</pre>
</html>
<?php
$name = $_GET['name'];
$url = $_SERVER['QUERY_STRING'];
if (isset($name)){
    if (preg_match('/\.|etc|var|tmp|usr/i', $url)){
        echo("hacker!");
    }
    else{
        if (preg_match('/base|class|file|function|index|upload_file/i', $name)){
            echo ("hacker!");
        }
        else{
            $name = safe_replace($name);
            if (preg_match('/base|class|file|function|index|upload_file/i', $name)){
                $filename = $name.'.php'; //获取文件名称
                $dir ="./";  //相对于网站根目录的下载目录路径
                $down_host = $_SERVER['HTTP_HOST'].'/'; //当前域名
                //判断如果文件存在,则跳转到下载路径
                if(file_exists(__DIR__.'/'.$dir.$filename)){
                    $file = fopen ( $dir.$filename, "rb" );

                    //告诉浏览器这是一个文件流格式的文件
                    Header ( "Content-type: application/octet-stream" );
                    //请求范围的度量单位
                    Header ( "Accept-Ranges: bytes" );
                    //Content-Length是指定包含于请求或响应中数据的字节长度
                    Header ( "Accept-Length: " . filesize ( $dir.$filename ) );
                    //用来告诉浏览器，文件是可以当做附件被下载，下载后的文件名称为$file_name该变量的值。
                    Header ( "Content-Disposition: attachment; filename=" . $filename );

                    //读取文件内容并直接输出到浏览器
                    echo fread ( $file, filesize ( $dir . $filename ) );
                    fclose ( $file );
                    exit ();
                }else{
                    echo ("file doesn't exist.");
                }
            }
            if (preg_match('/flag/i', $name)){
                echo ("hacker!");
            }
        }
    }
}


//return safe name
function safe_replace($string) {
    $string = str_replace('%20','&quot;',$string);
    $string = str_replace('%27','&quot;',$string);
    $string = str_replace('%2527','&quot;',$string);
    $string = str_replace('*','&quot;',$string);
    $string = str_replace('"','&quot;',$string);
    $string = str_replace("'",'&quot;',$string);
    $string = str_replace('"','&quot;',$string);
    $string = str_replace(';','&quot;',$string);
    $string = str_replace('<','&lt;',$string);
    $string = str_replace('>','&gt;',$string);
    $string = str_replace("{",'&quot;',$string);
    $string = str_replace('}','&quot;',$string);
    $string = str_replace('\\','',$string);
    return $string;
}
