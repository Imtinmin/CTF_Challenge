<?php 

/**
* 用户控制器
*/
class UserController extends BaseController
{
	// 访问列表
	public function actionList()
	{
		$params = $_REQUEST;
		$userModel = new UserModel();
		$listData = $userModel->getPageList($params);
		$this->loadView('userList', $listData );
	}
    public function actionIndex()
    {
        $listData = $_REQUEST;
        $this->loadView('userIndex',$listData);
    }

}