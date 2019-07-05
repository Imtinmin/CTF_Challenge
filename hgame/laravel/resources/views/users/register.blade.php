@extends('layouts.default')

@section('content')
    <div class="content">
        <div class="content">
            <div class="title m-b-md">
                Register
            </div>
        </div>
        @include('shared._errors')
        <form method="POST" action="{{ route('users.store') }}">
            {{ csrf_field() }}
            <div class="form-group">
                <input type="text" name="name" style="margin-bottom:10px;width:270px;height:20px;font-size: 17px" value="{{ old('name') }}" placeholder="name">
            </div>
            <div class="form-group">
                <input type="email" name="email" style="margin-bottom:10px;width:270px;height:20px;font-size: 17px" value="{{ old('email') }}"  placeholder="email">
            </div>
            <div class="form-group">
                <input type="password" name="password" style="margin-bottom:10px;width:270px;height:20px;font-size: 17px" value="{{ old('password') }}"  placeholder="password">
            </div>
            <div class="form-group">
                <input type="password" name="password_confirmation" style="margin-bottom:10px;width:270px;height:20px;font-size: 17px" value="{{ old('password_confirmation') }}"  placeholder="confirm your password">
            </div>
            <button type="submit" class="button">register</button>
        </form>
    </div>
@stop