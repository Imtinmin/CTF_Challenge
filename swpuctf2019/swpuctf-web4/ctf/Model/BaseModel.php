<?php 

class BaseModel
{
    public $safe;
    public function __construct()
    {
        $this->safe = new Safe();
    }
}