<?php


class LoginModel extends BaseModel
{
    public function getPassword($username)
    {
        if ($this->loginCheck()) {
            return "ok";
        }
        $dbTool = new DBTool("user");
        return $dbTool->getPassword($username);

    }
    public function loadView($viewName ='', $message = [])
    {
        $this->viewPath = BASE_PATH . "/View/{$viewName}.php";
        if(file_exists($this->viewPath))
        {
            $msg = $message;
            include $this->viewPath;
        }
    }
    public function loginCheck()
    {
        if($_SESSION['name']) {
            return true;
        } else {
            return false;
        }
    }
}