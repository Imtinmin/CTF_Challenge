<?php 

class UserModel extends BaseModel
{
	// 获取列表
	public function getPageList($params = [])
	{
		$pageData = [];
		$dbTool = new DBTool('user');

		$page = isset($params['page']) ? $params['page'] : 1;
		$size = isset($params['size']) ? $params['size'] : DEFAULT_PAGE_SIZE;
		
		$params['page'] = $page;
		$params['size'] = $size;
		$pageData['countTotal'] = $dbTool->getCountTotal($params);
		// D($pageData);
		//$p=new Page(总页数,显示页数,当前页码,每页显示条数,[链接]);
		//连接不设置则为当前链接
		$page = new Page($pageData['countTotal'],5,$page, $size);
		// //生成一个页码样式（可添加自定义样式）
		// //样式 共45条记录,每页显示10条,当前第1/4页 [首页] [上页] [1] [2] [3] .. [下页] [尾页]
		// echo $p->showPages(1);   

		$pageData['page'] = $page;
		$pageData['list'] = $dbTool->getList($params);
		return $pageData;
	}
}