<?php
//生成优惠码
$_SESSION['seed']=238059335;
function youhuima(){
	mt_srand($_SESSION['seed']);
    $str_rand = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $auth='';
    $len=25;
    for ( $i = 0; $i < $len; $i++ ){
        if($i<=($len/2))
              $auth.=substr($str_rand,mt_rand(0, strlen($str_rand) - 1), 1);
              //echo $auth;
        else
              $auth.=substr($str_rand,(mt_rand(0, strlen($str_rand) - 1))*-1, 1);
              //echo $auth; 
    }
    //setcookie('Auth', $auth); 7O8kTuoVbLefu0H6gSHeZdjd
}
echo $auth;
//support
	if (preg_match("/^\d+\.\d+\.\d+\.\d+$/im",$ip)){
        if (!preg_match("/\?|flag|}|cat|echo|\*/i",$ip)){
               //执行命令     ip=1.1.1.1%0ac'a't /f'l'ag    ip=1.1.1.1%0aa=ca;b=t;c=/fl;d=ag;$a$b $c$d
            
        }else {
              //flag字段和某些字符被过滤!
        }
	}else{
             // 你的输入不正确!
	}
?>
