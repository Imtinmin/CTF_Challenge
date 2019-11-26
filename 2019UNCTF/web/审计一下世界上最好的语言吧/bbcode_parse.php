<?php

$tag_parse_func = [
'b_tag_decode',
'em_tag_decode',
'video_tag_decode',
'url_tag_decode',
];

function b_tag_decode($code){
	return preg_replace_callback(
		"/\[b\](.+)\[\/b\]/", 
		function($a){
			return "<b>".htmlentities($a[1])."</b>";
		}, 
		$code);
}

function em_tag_decode($code){
	return preg_replace_callback(
		"/\[em\](.+)\[\/em\]/", 
		function($a){
			return "<em>".htmlentities($a[1])."</em>";
		}, 
		$code);
}

function url_tag_decode($code){
	// $code = htmlentities($code);
	return preg_replace_callback(
		"/\[url\](.+)\[\/url\]/", 
		function($a){
			$a[1] = str_replace("'","",$a[1]);
			$a[1] = str_replace("javascript:","",$a[1]);
			return "<a href='$a[1]'>".htmlentities($a[1])."</a>";
		}, 
		$code);

	return $code;
}

function parse_video_code($url){
	$ret_url = "";
	$parsed_url = parse_url(urldecode($url));

	if (isset($parsed_url['query'])) {

		$queries = explode("&", $parsed_url['query']);
		$input = array();
		foreach($queries as $query)
		{
			list($key, $value) = explode("=", $query);
			$key = str_replace("amp;", "", $key);
			$input[$key] = $value;
		}
	}

	if (isset($parsed_url['fragment'])) {
		$fragments = array();
		if($parsed_url['fragment'])
		{
			$fragments = explode("&", $parsed_url['fragment']);
		}
	}
	
	if (isset($parsed_url['path'])) {
		$path = explode('/', $parsed_url['path']);
	}
	

	switch ($parsed_url['host']) {
		case 'www.youtube.com':
			$template_html = "<video src='https://www.youtube.com/embed/{id}'></video>";
			if(isset($fragments[0]))
			{
				$id = str_replace('!v=', '', $fragments[0]); // http://www.youtube.com/watch#!v=fds123
			}
			elseif(isset($input['v']))
			{
				$id = $input['v']; // http://www.youtube.com/watch?v=fds123
			}
			else
			{
				$id = isset($path[1])?:"niubi"; // http://www.youtu.be/fds123
			}
			$ret_url = str_replace('{id}',$id,$template_html);
			break;
		
		default:
			# code...
			return "video?";
	}

	return $ret_url;
	
}

function video_tag_decode($code){
	$video_tag_preg = "/\[video\](.*?)\[\/video\]/";
	// example : https://youtube.com/xixi?v=123123
	$parsed = array();
	$n = preg_match_all($video_tag_preg,$code,$videos);
	if($n){
		foreach ($videos[1] as $key => $value) {
			$html = parse_video_code($value);
			$code = str_replace($videos[0][$key],$html,$code);
		}
	}
	return $code;
}

function parse_code($content){
	global $tag_parse_func;
	foreach ($tag_parse_func as $func) {
		$content = $func($content);
	}
	return $content;
}
