<?php

include("inc_common.php");

function Where1sFl4g() {
    $secret = "):.jbax g'abq V";
    echo str_rot13(strrev($secret));
}

function save($t) {
    if(strlen($t) > 100) die("Bad H4ck3r");
    if(strlen($t) < 10) die("Bad H4ck3r");
    file_put_contents("/tmp/bad", $t);
}

function isSupportFileSize($f) {
    return @filesize($f);
}

function getContentType($mimes,$fn)
{
    global $mimes;
    $fileInfo = pathinfo($fn);
    $ext = strtolower($fileInfo['extension']);

    foreach ($mimes as $k=>$v)
    {
        if ($k == $ext)
        {
            return $v;
        }
    }
    return false;
}

function getContentTypeByExtension($mimes,$ext)
{
    global $mimes;

    foreach ($mimes as $k=>$v)
    {
        if ($k == $ext)
        {
            return $v;
        }
    }
    return false;
}

function getFilename($path){
    $pos = strrpos($path,'/');
    if($pos === false){
        return false;
    }
    $len = strlen($path);
    if($len < $pos){
        return false;
    }else{
        $filename=substr($path,$pos+1,$len-$pos-1);
        return $filename;
    }
}

function isValidPath($path)
{
    return (strstr($path,"/../") != false)?false:true;
}

function getLastFolder($path)
{
    $offset = Array();

    for ($i=(strlen($path)-1);$i>0;$i--)
    {
        if (substr($path,$i,1) == '/')
        {
            $offset[] = $i;
        }
    }

    if (count($offset) >= 2)
    {
        return substr($path,($offset[1]+1),($offset[0]-$offset[1]-1));
    } else {
        return '';
    }

}

function proc_kill( $pid ) {	
    if ( $pid > 0){
        $command = "/bin/kill " . $pid . " 2>/dev/null";
        $ret = shell_exec( $command );
        return true;
    }
    return false;
}

function print_title($r) {
    if(isset($r)) {
        echo $r->body->title;
    }
}

function print_content($r) {
    if(isset($r)) {
        echo $r->body->content;
    }
}

function getFileNameWithoutExt($fn)
{
    $fnLen = strlen($fn);
    $findPoint = false;

    for ($t=($fnLen-1);$t>=0;$t--)
    {
        if (substr($fn,$t,1) == '.')
        {
            $findPoint = true;
            break;
        }
    }

    if ($findPoint === true)
        return substr($fn,0,$t);
    return $fn;
}

function sortCmp($a,$b)
{
    global $SORT_KEY;
    return strnatcasecmp($a[$SORT_KEY], $b[$SORT_KEY]);
}

function saveSortSetting($sortItem,$sortType,$CLASS,$DB,$dbTables)
{	
    $CLASS->saveSetting($sortItem,$sortType);
}

function getFilePathFull($fileRoot,$path)
{
    return $fileRoot . $path;
}

function getClientIP()
{
    static $realip = NULL;

    if ($realip !== NULL )
        return $realip;

    if (isset($_SERVER))
    {
        if (isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        {
            $arr = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);

            foreach ($arr AS $ip)
            {
                $ip = trim($ip);

                if ($ip != 'unknown')
                {
                    $realip = $ip;
                    break;
                }
            }
        } else if (isset($_SERVER['HTTP_CLIENT_IP'])) {
            $realip = $_SERVER['HTTP_CLIENT_IP'];
        } else {
            if (isset($_SERVER['REMOTE_ADDR']))
                $realip = $_SERVER['REMOTE_ADDR'];
            else
                $realip = '0.0.0.0';
        }
    } else {
        if (getenv('HTTP_X_FORWARDED_FOR'))
            $realip = getenv('HTTP_X_FORWARDED_FOR');
        elseif (getenv('HTTP_CLIENT_IP'))
            $realip = getenv('HTTP_CLIENT_IP');
        else
            $realip = getenv('REMOTE_ADDR');
    }
    preg_match("/[\d\.]{7,15}/", $realip, $onlineip);
    $realip = !empty($onlineip[0]) ? $onlineip[0] : '0.0.0.0';

    return $realip;
}

function MyTrim($str)
{
    $str = trim($str);
    return $str;
}

function johncena() 
{
    header("Location: ".str_rot13("uggcf://jjj.lbhghor.pbz/jngpu?i=KtHO3yS9VDN"));
}

function lockFileExist($lockPath)
{
		if (file_exists($lockPath))
				return true;
		else
				return false;
}

function unLockFile($lockPath)
{
		if (file_exists($lockPath))
				unlink($lockPath);
		return true;
}

function showWrongPass($wrong) {
		if($wrong === true) {
				echo "<div class='alert'>Wrong username or password!</div>";
		}
}

function showWrongReg($wrong) {
    if($wrong === true) {
                 echo "<div class='alert'>Sorry, Register Closed!</div><br>";
    }
}

function headerNotFound($msg='')
{
	header('HTTP/1.1 404 Not Found');
	echo '[ 404 Not Found ] '.$msg;
}

function headerUnauthorized($msg='')
{
	header('HTTP/1.1 401 Unauthorized');
	echo '[ 401 Unauthorized ] '.$msg;
}
