<?php

$template_html = file_get_contents("template.html");

function parseStrIf($strIf)
	{
		if(strpos($strIf,'=')===false)
		{
			return $strIf;
		}
		if((strpos($strIf,'==')===false)&&(strpos($strIf,'=')>0))
		{
			$strIf=str_replace('=', '==', $strIf);
		}
		$strIfArr =  explode('==',$strIf);
		return (empty($strIfArr[0])?'NULL':$strIfArr[0])."==".(empty($strIfArr[1])?'NULL':$strIfArr[1]);
	}

function parseIf($content){
	if (strpos($content,'{if:')=== false){
            return $content;
    }else{
        $Rule = "/{if:(.*?)}(.*?){end if}/is";
        preg_match_all($Rule,$content,$iar);
        $arlen=count($iar[0]);
        $elseIfFlag=false;
        for($m=0;$m<$arlen;$m++){
            $strIf=$iar[1][$m];
            $strIf=parseStrIf($strIf);
            @eval("if(".$strIf.") { \$ifFlag=true;} else{ \$ifFlag=false;}");
        }
    }
    return $content;
}

function parse_again(){
	global $template_html,$searchword;
	$searchnum 	= isset($GLOBALS['searchnum'])?$GLOBALS['searchnum']:"";
	$type 		= isset($GLOBALS['type'])?$GLOBALS['type']:"";
	$typename 	= isset($GLOBALS['typename'])?$GLOBALS['typename']:"";


	$searchword = substr(RemoveXSS($searchword),0,20);
	$searchnum = substr(RemoveXSS($searchnum),0,20);
	$type = substr(RemoveXSS($type),0,20);
	$typename = substr(RemoveXSS($typename),0,20);
	$template_html = str_replace("{haha:searchword}",$searchword,$template_html);
	$template_html = str_replace("{haha:searchnum}",$searchnum,$template_html);
	$template_html = str_replace("{haha:type}",$type,$template_html);
	$template_html = str_replace("{haha:typename}",$typename,$template_html);
	$template_html = parseIf($template_html);
	return $template_html;
}