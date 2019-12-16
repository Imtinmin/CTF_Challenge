<?php 

/**
* 所有控制器的父类
*/
class BaseController
{
	/*
	 * 加载视图文件
	 * viewName 视图名称
	 * viewData 视图分配数据
	*/
	private $viewPath;
	public function loadView($viewName ='', $viewData = [])
	{
		$this->viewPath = BASE_PATH . "/View/{$viewName}.php";
		if(file_exists($this->viewPath))
		{
			extract($viewData);
			include $this->viewPath;
		}
	}
	
}