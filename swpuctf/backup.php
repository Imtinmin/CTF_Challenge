<?php
include("upload.php");
echo "上传目录：" . $upload_dir . "<br />";
$sys = "tar -czf z.tar.gz *";
chdir($upload_dir);
system($sys);
if(file_exists('z.tar.gz')){
	echo "上传目录下的所有文件备份成功!<br />";
	echo "备份文件名: z.tar.gz";
}else{
	echo "未上传文件，无法备份！";
}
?>
