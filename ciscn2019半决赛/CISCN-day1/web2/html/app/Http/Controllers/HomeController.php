<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Cookie;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Input;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $current_user = Auth::user()->name;
        if ($current_user === "admin") {
            $this->admin_home();
            return view("admin");
        } else {
            $this->user_home($current_user);
            return view('home');
        }
    }

    public function admin_home()
    {
        Cookie::queue("laravel_session", Cookie::get("laravel_session"), 3600);
        $user_info = DB::table("users_online")->where("name", "admin")->first();
        if (empty($user_info)) {
            DB::table("users_online")->insert(
                ["name" => "admin", "laravel_session" => $this->validation($_COOKIE['laravel_session']), 'created_at' => date('Y-m-d h:i:s', time())]
            );
        }else{
            DB::table("users_online")->where("name","admin")->update(
                ["laravel_session" => $this->validation($_COOKIE['laravel_session']), 'created_at' => date('Y-m-d h:i:s', time())]
            );
        }
    }

    public function user_home($current_user)
    {
        //Cookie::queue("laravel_session", Cookie::get("laravel_session"), 3600);
        $user_info = DB::table("users_online")->where("name", $current_user)->first();
        if (empty($user_info)) {
            DB::table("users_online")->insert(
                ["name" => $current_user, "laravel_session" => $this->validation($_COOKIE['laravel_session']), 'created_at' => date('Y-m-d h:i:s', time())]
            );
        }
    }

    public function upload(Request $request)
    {
        if ($request->isMethod('post')) {
            $file = $request->file('file');
            $dir=md5($this->getIp());
            chdir("uploads");
            if(!is_dir($dir)){
                @mkdir($dir);
            }
            chdir($dir);
            $upload_file_name=$dir.".jpg";
            move_uploaded_file($file->getRealPath(),getcwd()."/".$upload_file_name);
            $upload_jpg=getcwd()."/".$upload_file_name;
            $error=$file->isValid();
            $filesize=filesize($upload_jpg);
            $file_ext=$file->getClientOriginalExtension();
            if(strstr(file_get_contents($upload_jpg),"php")!==False){
                if(strstr(file_get_contents($upload_jpg),"eval")!==False){
                    unlink($upload_jpg);
                }
                return view('admin',["error"=>"I found the eval string in the file, which has been deleted."]);
            }
            if($error or $file_ext !== "jpg" or $filesize>0){
                sleep(1);
                unlink($upload_jpg);
            }
            return view('admin',["upload_file"=>"success","hash"=>$dir]);
        } else {
            return redirect('index');
        }
    }

    public function online_upload(Request $request){
        if ($request->isMethod('post')) {
            if(!empty($request->input("url"))){
                $url=$request->input("url");
                if(preg_match("/^(file|phar|glob|file|php|data|expect).*$/i",$url)){
                    return view("admin",['online_upload'=>1,'error'=>'Illegal URL!']);
                }else{
                    $pic_info=getimagesize($url);
                    if($pic_info['mime']=="wisdomtree/test"){
                        $dir=md5($this->getIp());
                        chdir("uploads");
                        if(!is_dir($dir)){
                            @mkdir($dir);
                        }
                        chdir($dir);
                        $upload_file_name=md5(rand(1,1000)).".jpg";
                        file_put_contents($upload_file_name,file_get_contents($pic_info));
                        if(filesize($upload_file_name)>0){
                            unlink($upload_file_name);
                        }
                    }else{
                        return view("admin",['online_upload'=>1,'error'=>"Only MIME is 'wisdomtree/test' can be uploaded!"]);
                    }
                }
            }else{
                return view("admin",['online_upload'=>1,'error'=>'Url is empty!']);
            }
        }else{
            return view("admin",['online_upload'=>1]);
        }
    }

    public function find()
    {
        if (Input::method() === "POST") {
            $username = $this->waf(Input::get("username"));
            $current_user = Auth::user()->name;
            $find_info = DB::table("users_online")->whereRaw("name='$username'")->first();
            if ($find_info !== null) {
                if ($find_info->name !== $current_user) {
                    $find_info->laravel_session = "************";
                }
                return view('home', ['id' => $find_info->id, 'name' => $find_info->name, 'laravel_session' => $find_info->laravel_session, 'created_at' => $find_info->created_at]);
            } else {
                return view("home");
            }
        } else {
            return redirect("index");
        }
    }

    private function validation($laravel_session)
    {
        $patter = "#^([A-Za-z0-9+\/]{4})*([A-Za-z0-9+\/]{4}|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}==)$#i";
        $patch = preg_match($patter, $laravel_session);
        if ($patch) {
            return $laravel_session;
        } else {
            return "";
        }
    }

    private function waf($sql)
    {
        $petter = "\ |and|or|\|\||\&\&|<|>|=|benchmark|sleep|join|union|if";
        $match = preg_replace("/$petter/i", '', $sql);
        return $match;
    }

    public function getIp()
    {
        if (!empty($_SERVER["HTTP_CLIENT_IP"])) {
            $cip = $_SERVER["HTTP_CLIENT_IP"];
        } else if (!empty($_SERVER["HTTP_X_FORWARDED_FOR"])) {
            $cip = $_SERVER["HTTP_X_FORWARDED_FOR"];
        } else if (!empty($_SERVER["REMOTE_ADDR"])) {
            $cip = $_SERVER["REMOTE_ADDR"];
        } else {
            $cip = '';
        }
        preg_match("/[\d\.]{7,15}/", $cip, $cips);
        $cip = isset($cips[0]) ? $cips[0] : 'unknown';
        unset($cips);
        return $cip;
    }
}
