@extends('layouts.default')

@section('content')
    <div class="content">
        <div class="content">
            <div class="title m-b-md">
                Login
            </div>
        </div>
        <div style="text-align: center;font-size: 30px;">
            @include('shared._messages')
        </div>
        <form method="POST" action="{{ route('login') }}">
            {{ csrf_field() }}
            <div class="form-group">
                <input type="email" name="email" style="margin-bottom:10px;width:270px;height:20px;font-size: 17px" value="{{ old('email') }}"  placeholder="email">
            </div>
            <div class="form-group">
                <input type="password" name="password" style="margin-bottom:10px;width:270px;height:20px;font-size: 17px" value="{{ old('password') }}"  placeholder="password">
            </div>
            <button type="submit" class="button">login</button>
        </form>
    </div>
@stop
