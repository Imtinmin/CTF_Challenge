<?php


$black_list = ['|','&','"','\'','select','union',';','`','$','\\'];
$extension_list = ['.png','.gif','.jpg','.css'];
$url = $_GET['f'];
$urlInfo = parse_url($url);

if(!("http" === strtolower($urlInfo["scheme"]) || "https"===strtolower($urlInfo["scheme"]))){    
  die( "scheme error!");
}

for ($i=0; $i < sizeof($black_list); $i++) { 
    // var_dump($black_list[$i]);
    if(strpos($url,$black_list[$i])){
        die('hacker!');
    }
}

$flag = 0;

for ($i=0; $i < sizeof($extension_list); $i++) { 
    if(substr($url,-4,4)===$extension_list[$i]){
        $flag = 1;
        break;
    }
}

if($flag){
    system("curl ".$url);
}else{
    die('support only static file type!');
}

?>

