<?php

function RemoveXSS($val) {
    // remove all non-printable characters. CR(0a) and LF(0b) and TAB(9) are allowed  
    // this prevents some character re-spacing such as <java\0script>  
    // note that you have to handle splits with \n, \r, and \t later since they *are* allowed in some inputs  
    $val = preg_replace('/([\x00-\x08,\x0b-\x0c,\x0e-\x19])/', '', $val);

    // straight replacements, the user should never need these since they're normal characters  
    // this prevents like <IMG SRC=@avascript:alert('XSS')>  
    $search = 'abcdefghijklmnopqrstuvwxyz';
    $search .= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $search .= '1234567890!@#$%^&*()';
    $search .= '~`";:?+/={}[]-_|\'\\';
    for ($i = 0; $i < strlen($search); $i++) {
        // ;? matches the ;, which is optional 
        // 0{0,7} matches any padded zeros, which are optional and go up to 8 chars 

        // @ @ search for the hex values 
        $val = preg_replace('/(&#[xX]0{0,8}'.dechex(ord($search[$i])).';?)/i', $search[$i], $val); // with a ; 
        // @ @ 0{0,7} matches '0' zero to seven times  
        $val = preg_replace('/(&#0{0,8}'.ord($search[$i]).';?)/', $search[$i], $val); // with a ; 
    }

    // now the only remaining whitespace attacks are \t, \n, and \r 

    $ra1 = Array('_GET','_POST','_COOKIE','_REQUEST','if:','javascript', 'vbscript', 'expression', 'applet', 'meta', 'xml', 'blink', 'link', 'style', 'script', 'embed', 'object', 'iframe', 'frame', 'frameset', 'ilayer', 'layer', 'bgsound', 'title', 'base', 'eval', 'passthru', 'exec', 'assert', 'system', 'chroot', 'chgrp', 'chown', 'shell_exec', 'proc_open', 'ini_restore', 'dl', 'readlink', 'symlink', 'popen', 'stream_socket_server', 'pfsockopen', 'putenv', 'cmd','base64_decode','fopen','fputs','replace','input','contents');
    $ra2 = Array('onabort', 'onactivate', 'onafterprint', 'onafterupdate', 'onbeforeactivate', 'onbeforecopy', 'onbeforecut', 'onbeforedeactivate', 'onbeforeeditfocus', 'onbeforepaste', 'onbeforeprint', 'onbeforeunload', 'onbeforeupdate', 'onblur', 'onbounce', 'oncellchange', 'onchange', 'onclick', 'oncontextmenu', 'oncontrolselect', 'oncopy', 'oncut', 'ondataavailable', 'ondatasetchanged', 'ondatasetcomplete', 'ondblclick', 'ondeactivate', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'onerror', 'onerrorupdate', 'onfilterchange', 'onfinish', 'onfocus', 'onfocusin', 'onfocusout', 'onhelp', 'onkeydown', 'onkeypress', 'onkeyup', 'onlayoutcomplete', 'onload', 'onlosecapture', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onmove', 'onmoveend', 'onmovestart', 'onpaste', 'onpropertychange', 'onreadystatechange', 'onreset', 'onresize', 'onresizeend', 'onresizestart', 'onrowenter', 'onrowexit', 'onrowsdelete', 'onrowsinserted', 'onscroll', 'onselect', 'onselectionchange', 'onselectstart', 'onstart', 'onstop', 'onsubmit', 'onunload');
    $ra = array_merge($ra1, $ra2);

    $val_before = $val;
    for ($i = 0; $i < sizeof($ra); $i++) {
        $pattern = '/'.$ra[$i].'/i';
        $replacement = substr($ra[$i], 0, 2).'<x>'.substr($ra[$i], 2); // add in <> to nerf the tag  
        $val = preg_replace($pattern, $replacement, $val); // filter out the hex tags  
    }
    return $val;
}
function check_var($arr){
    $deny = array("_GET","_POST","GLOBALS");
    foreach ($arr as $key => $value) {
        if (in_array($key,$deny)){
            exit("no no no");
        }
    }
}

check_var($_GET);
check_var($_POST);
check_var($_COOKIE);
foreach (['_GET','_POST','_COOKIE'] as $v) {
    foreach ($$v as $key => $value) {
        $$key = $value;
    }
}



