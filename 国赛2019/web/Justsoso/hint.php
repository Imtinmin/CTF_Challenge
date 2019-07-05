<?php  
class Handle{ 
    private $handle;  
    public function __wakeup(){
		foreach(get_object_vars($this) as $k => $v) {
            $this->$k = null;
        }
        echo "Waking up\n";
    }
	public function __construct($handle) { 
        $this->handle = $handle; 
    } 
	public function __destruct(){
		$this->handle->getFlag();
	}
}

class Flag{
    public $file;
    public $token;
    public $token_flag;
 
    function __construct($file){
		$this->file = $file;
		$this->token_flag = $this->token = md5(rand(1,10000));
    }
    
	public function getFlag(){
		$this->token_flag = md5(rand(1,10000));
        if($this->token === $this->token_flag)
		{
			if(isset($this->file)){
				echo @highlight_file($this->file,true); 
            }  
        }
    }
}
?>