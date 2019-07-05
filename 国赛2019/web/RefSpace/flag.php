<?php
if (!defined('LFI')) {
    echo "Include me!";
    exit();
}
use interesting\FlagSDK;
$sdk = new FlagSDK();
$key = $_GET['key'] ?? false;
if (!$key) {
    echo "Please provide access key<br \>";
    echo '$_GET["key"];';
    exit();
}
$flag = $sdk->verify($key);
if ($flag) {
    echo $flag;
} else {
    echo "Wrong Key";
    exit();
}
//Do you want to know more about this SDK?
//we 'accidentally' save a backup.zip for more information
