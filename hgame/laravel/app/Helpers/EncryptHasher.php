<?php

namespace App\Helpers;

use Illuminate\Hashing\AbstractHasher;
use Illuminate\Contracts\Hashing\Hasher as HasherContract;

class EncryptHasher extends AbstractHasher implements  HasherContract
{
    protected $rounds = 10;
    protected $verifyAlgorithm = false;
    public function __construct(array $options = [])
    {
        $this->rounds = $options['rounds'] ?? $this->rounds;
        $this->verifyAlgorithm = $options['verify'] ?? $this->verifyAlgorithm;
    }
    public function check($value, $hashedValue, array $options = [])
    {

        return $this->make($value) === decrypt($hashedValue);
    }

    public function needsRehash($hashedValue, array $options = [])
    {
        return false;
    }

    public function make($value, array $options = [])
    {
        return $value;
    }
    public function setRounds($rounds)
    {
        $this->rounds = (int) $rounds;

        return $this;
    }
}