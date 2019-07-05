<?php
$_SESSION['seed']=rand(0,999999999);
$len = 15;
//$i = 1;
/*if ($i<=($len/2)){
	echo 'Oh';
}else{
	echo 'no';
}*/
$youhuima = "OQ4HYwBanhGLKKs";
$str_rand = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$auth = '';
for ($seed = 0; $seed < 999999999; $seed++){
	mt_srand($seed);
	for ( $i = 0; $i < $len; $i++ ){
    	if($i<=($len/2)){
            $auth.=substr($str_rand,mt_rand(0, strlen($str_rand) - 1), 1);
            //echo $auth;	
    	}else{
    	    $auth.=substr($str_rand,(mt_rand(0, strlen($str_rand) - 1))*-1, 1);
            //echo $auth;
    	}
    }
    if ($auth === $youhuima){
    	echo $seed;
    }else{
    	unset ($i);
    }
}

