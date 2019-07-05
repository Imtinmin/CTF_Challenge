<?php
error_reporting(0);
class come{    
    private $method;
    private $args;
    function __construct($method, $args) {
        $this->method = $method;
        $this->args = $args;
    }
    function __wakeup(){
        foreach($this->args as $k => $v) {
            $this->args[$k] = $this->waf(trim($v));
        }
    }
    function waf($str){
        $str=preg_replace("/[<>*;|?\n ]/","",$str);
        $str=str_replace('flag','',$str);
        return $str;
    }           
    function echo($host){
        system("echo $host");
    }
    function __destruct(){
        if (in_array($this->method, array("echo"))) {
            call_user_func_array(array($this, $this->method), $this->args);
        }
    } 

}

$first='hi';
$var='var';
$bbb='bbb';
$ccc='ccc';
$i=1;
foreach($_GET as $key => $value) {
        if($i===1)
        {
            $i++;
            $$key = $value;
        }
        else{break;}
}
if($first==="doller")
{
    @parse_str($_GET['a']);
    if($var==="give")
    {
        if($bbb==="me")
        {
            if($ccc==="flag")
            {
                echo "<br>welcome!<br>";
                $come=@$_POST['come'];
                unserialize($come); 
            }
        }
        else
        {echo "<br>think about it<br>";}
    }
    else
    {
        echo "NO";
    }


}
else
{
    echo "Can you hack me?<br>";
}

