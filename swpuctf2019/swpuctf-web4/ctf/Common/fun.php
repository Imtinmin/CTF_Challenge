<?php  



// 调试函数
if(!file_exists('D'))
{
	function D()
	{
		echo '<pre>';
		print_r(func_get_args());
		echo '</pre>';
	}
}

// 注册自动加载
if(!file_exists('user_aotu_load'))
{
	function user_aotu_load($className)
	{
		$classPath = 'Lib';
		if(strrpos($className, 'Controller') !== FALSE )
		{
			$classPath = 'Controller';
		}
		else if(strrpos($className, 'Model') !== FALSE )
		{
			$classPath = 'Model';
		}
		$classPath = BASE_PATH . "/{$classPath}/{$className}.php";
		if(file_exists($classPath))
		{
			include $classPath;
		}
	}
	spl_autoload_register('user_aotu_load');
}



// 路由控制跳转至控制器
if(!empty($_REQUEST['r']))
{
	$r = explode('/', $_REQUEST['r']);
	list($controller,$action) = $r;
	$controller = "{$controller}Controller";
	$action = "action{$action}";


	if(class_exists($controller))
	{
		if(method_exists($controller,$action))
		{
			//
		}
		else
		{
			$action = "actionIndex";
		}
	}
	else
	{
		$controller = "LoginController";
        $action = "actionIndex";
	}
    $data = call_user_func(array( (new $controller), $action));
} else {
    header("Location:index.php?r=Login/Index");
}
