<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use DB;

class UsersController extends Controller
{
    public function register()
    {
        return view('users.register');
    }
    public function login()
    {
        return view('users.login');
    }
    public function show()
    {
        return view('users.show');
    }
    public function store(Request $request)
    {
        $this->validate($request, [
            'name' => 'required|min:4|max:100',
            'email' => 'required|unique:users|min:6|max:100',
            'password' => 'required|confirmed|min:6|max:20'
        ]);

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => encrypt($request->password),
        ]);
        return redirect()->route('login');
    }
}
