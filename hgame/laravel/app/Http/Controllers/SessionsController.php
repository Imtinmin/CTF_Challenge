<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use Auth;
use DB;
use think\response\Redirect;

class SessionsController extends Controller
{
    public function store(Request $request)
    {
        $credentials = $this->validate($request, [
            'email' => 'required|email|max:100',
            'password' => 'required'
        ]);

        if (Auth::attempt($credentials)) {
            if (Auth::user()->id ===1){
                session()->flash('info','flag :******');
                return redirect()->route('users.show');
            }
            $name = DB::select("SELECT name FROM `users` WHERE `name`='".Auth::user()->name."'");
            session()->flash('info', 'hello '.$name[0]->name);
            return redirect()->route('users.show');
        } else {
            session()->flash('danger', 'sorry,login failed');
            return redirect()->back()->withInput();
        }
    }
    public function destroy()
    {
        Auth::logout();
        session()->flash('success', 'logout success');
        return redirect('login');
    }
}
