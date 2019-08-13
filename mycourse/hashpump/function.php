<?php
//function.php
function waf($arr){
    foreach ($arr as $key => $value) {
        $value = preg_replace('/a/','',$value);
        $_REQUEST[$key] = $value;
    }
    return $_REQUEST;
}

function checksign($secret,$action,$filename,$sign){
    //echo md5($secret.$filename.$action);
    if(md5($secret.$filename.$action) == $sign){
        return True;
    }else{
        return False;
    }
}

function getsign($str){
    return md5($str);
}
?>