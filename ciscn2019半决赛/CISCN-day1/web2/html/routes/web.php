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

Route::get('/', 'HomeController@index');

Route::post('/find', 'HomeController@find');

Route::get('/find', 'HomeController@find');

Route::post('/upload', 'HomeController@upload');

Route::get('/upload', 'HomeController@upload');

Route::post('/online_upload', 'HomeController@online_upload');

Route::get('/online_upload', 'HomeController@online_upload');

Route::get('/index', 'HomeController@index');
Auth::routes();
Route::get('/home', 'HomeController@index');
