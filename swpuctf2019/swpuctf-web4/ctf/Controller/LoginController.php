<?php


/*
 * 登陆控制器
 * */
class LoginController extends BaseController
{
    public function actionIndex()
    {
        $loginModel = new LoginModel();
        if( !$loginModel->loginCheck() ) {
            $this->loadView("userLogin");
            exit();
        } else {
            $this->loadView("userInfo", array("msg"=>array("code"=>"200","info"=>"login success!")));
        }
    }
    public function actionLogin()
    {
        $loginModel = new LoginModel();
        if( $loginModel->loginCheck() ) {
            $this->loadView("userInfo", array("msg"=>array("code"=>"200","info"=>"login success!")));
            exit();
        }
        $data = json_decode(file_get_contents("php://input"),true);
        $data['username'] = $loginModel->safe->check($data['username']);
        $password = $loginModel->getPassword($data['username']);
        if ( $password === $data['password'] && !empty($password) ) {
            $this->loadView("userInfo", array("msg"=>array("code"=>"200","info"=>"login success!")));
        } else {
            $this->loadView("userInfo", array("msg"=>array("code"=>"202","info"=>"error username or password.")));
        }
    }
    public function actionOut()
    {
        $this->loadView("userInfo", array("msg"=>array("code"=>"200","info"=>"login out success!")));
    }
}
