<a href="www.zip">source code</a>
<br/>
<?php

include("common.php");
include("bbcode_parse.php");
include("parse_template.php");
$c = parse_code(isset($GLOBALS['GLOBALS']['content'])?$GLOBALS['GLOBALS']['content']:"[b]hahha[/b]");


// 清除一些不必要的标签，方便判断 search 是否是独立出来的 html 标签
$c = preg_replace("/<em>.*?<\/em>/","",$c);
$c = preg_replace("/<b>.*?<\/b>/","",$c);
$c = preg_replace("/<video src='.*?'><\/video>/","",$c);
$c = preg_replace("/<a href='.*?'>/","",$c);

// search 必须是独立出来的标签哦~
$n = preg_match_all("/<search>(.*?)<\/search>/",$c,$searchword);
$searchnum=2;
if ($n>0) {
	$searchword = $searchword[1][0];
	if (strlen($searchword)>0){
		parse_again($searchword);
	}else{
		exit("searchword!!");
	}
}else{
	exit("input your searchword~");
}


