<?php
$payload = $_GET['payload'];
if(isset($payload)){  
    $url = parse_url($_SERVER['REQUEST_URI']);
    var_dump($url);
    parse_str($url['query'],$query);
    foreach($query as $value){
        var_dump($value);
        if (preg_match("/flag/",$value)) { 
    	    die('stop hacking!');
    	    exit();
        }
    }
    $payload = unserialize($payload);
    echo var_dump($payload);
}else{ 
   echo "Missing parameters"; 
} 