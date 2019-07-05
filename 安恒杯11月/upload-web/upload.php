<?php 
session_start();
if (isset($_SESSION['id'])){
	$id=$_SESSION['id'];
	if (isset($_POST['submit_file'])) {
		$file=$_FILES['file'];
		// print_r($file);
		$fileName=$_FILES['file']['name'];//$file['name']
		$fileTmpName=$_FILES['file']['tmp_name'];
		$fileSize=$_FILES['file']['size'];
		$fileError=$_FILES['file']['error'];
		$fileType=$_FILES['file']['type'];
		$fileExt=explode('.',$fileName);
		$fileActualExt=strtolower(end($fileExt));
		$baned=array('php');

		if (!in_array($fileActualExt,$baned)) {
			if($fileError===0){
				if($fileSize<1000000){
					$fileNameNew=$fileName;
					$fileDestination='uploads/'.$fileNameNew;
					move_uploaded_file($fileTmpName, $fileDestination);
					echo "You upload is save at:".$fileDestination;
				}else{
					echo "Your file is too big";
				}
			}else{
				echo "There was an error uploading your file!";
			}
		}else{
			echo "You cannot upload files of this type!";
		}
	}
}else{
	header("Location:index.php");
	exit();
}


 ?>