<?php  
@error_reporting(1); 
include 'flag.php';
class baby 
{   
    public $file;
    function __toString()      
    {          
        if(isset($this->file)) 
        {
            $filename = "./{$this->file}";        
            if (file_get_contents($filename))         
            {              
                return file_get_contents($filename); 
            } 
        }     
    }  
}  
if (isset($_GET['data']))  
{ 
    $data = $_GET['data'];
    preg_match('/[oc]:\d+:/i',$data,$matches);
    if(count($matches))
    {
        die('Hacker!');
    }
    else
    {
        $good = unserialize($data);
        echo $good;
    }     
} 
else 
{ 
    highlight_file("./index.php"); 
} 
?>