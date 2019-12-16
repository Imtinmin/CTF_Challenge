<?php

class Safe
{
    public function check($data)
    {
        if ( preg_match('/select|information|insert|union|ascii|,|like|outfile|join|<|>|and|substr|#|or|\|\||sleep|benchmark|if|&&/is', $data) )
        {
            return "test";
        } else {
            return $data;
        }
    }
}