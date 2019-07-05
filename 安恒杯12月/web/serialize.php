<?php
class baby 
{   
    public $file = 'flag.php';
    function __toString()

    {          
        $this->file;    
        if(isset($this->file)) 
        {
            $filename = "./{$this->file}";
            //print_r($filename);        
            if (file_get_contents($filename))         
            {              
                return file_get_contents($filename); 
            } 
        }     
    }  
}

$baby = new baby();
$a = serialize($baby);
echo $a;