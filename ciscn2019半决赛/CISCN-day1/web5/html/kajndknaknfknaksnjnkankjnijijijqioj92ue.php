<?php 
#highlight_file(__FILE__);
$ip=$_SERVER['REMOTE_ADDR'];
if ($ip != '127.0.0.1')
{
	die('this page can only be accessed by 127.0.0.1 <!-- hint xss -->');
}

function check_ip($url) 
{ 
    $match_result=preg_match('/^(http|gopher)?:\/\/.*(\/)?.*$/',$url); 
    if (!$match_result) 
    { 
        die('url format error'); 
    } 
    try 
    { 
        $url_parse=parse_url($url); 
    } 
    catch(Exception $e) 
    { 
        die('url fomat error'); 
    } 
    return false;
} 

function safe_request_url($url) 
{ 
     
    if (check_ip($url)) 
    { 
	echo $url.' is not ok!'; 
    } 
    else 
    {
        $ch = curl_init(); 

        curl_setopt($ch, CURLOPT_URL, $url); 
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
        curl_setopt($ch, CURLOPT_HEADER, 0); 
        $output = curl_exec($ch); 
        $result_info = curl_getinfo($ch); 
        if ($result_info['redirect_url']) 
        { 
            safe_request_url($result_info['redirect_url']); 
        } 
        curl_close($ch); 
        var_dump($output); 
    } 
     
} 
$url = $_GET['url']; 
#system("echo "+$url+" > /dev/shm/text");
if(!empty($url)){ 
    safe_request_url($url); 
} 

?>
