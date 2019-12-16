<?php 

// 单例设计模式，只连接一次数据库
class DBConnect 
{
    private static $_instance = null;
    //私有构造函数，防止外界实例化对象
    // private function __construct() {}
    //私有克隆函数，防止外办克隆对象
    // private function __clone() {}


    //静态方法，单例统一访问入口
    public static function getInstance() 
    {
       if(is_null(self::$_instance))
		{
			// D('tableName');
			self::$_instance = new PDO( DB_DSN, DB_USER, DB_PASSWORD);
		}
		return self::$_instance;
    }
}


class DBTool
{
	// 成员属性
	private $sqlCache;
	private $tableName;
	private $connect;
    private $safe;
	// 初始化对象
	public function __construct( $tableName = '')
	{
		// 连接数据库
		$this->tableName = $tableName;
		$this->connect = DBConnect::getInstance();
		$this->sqlCache = [];
	}

    //参数化
    public function prepare($sql)
    {
        $result = $this->connect->prepare($sql);
        return $result;
    }

    public function query($sql)
    {
        $res = $this->connect->query($sql);
        return $res;
    }

    public function fetch($result, $column_name)
    {
        $data = $result->fetch();
        return $data[$column_name];
    }

    public function getPassword( $username = '')
    {
        $sql = "select * from user where username=" . "'" . $username . "'";
        $res = self::query($sql);
        return self::fetch($res,"password");
    }

    public function __destruct()
    {
        // TODO: Implement __destruct() method.
        unset($this->connect);
    }
}
