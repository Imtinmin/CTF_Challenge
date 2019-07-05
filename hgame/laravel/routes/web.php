<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


Route::get('/', 'StaticPagesController@home')->name('home');
Route::get('/register','UsersController@register')->name('register');
Route::get('/login','UsersController@login')->name('login');
Route::get('/users', 'UsersController@show')->name('users.show');
Route::post('/users', 'UsersController@store')->name('users.store');
Route::post('/login', 'SessionsController@store')->name('login');
Route::get('/logout', 'SessionsController@destroy')->name('logout');