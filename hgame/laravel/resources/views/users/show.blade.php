@extends('layouts.default')

@section('content')
    @if (Auth::check())
        <div style="text-align: center;font-size: 30px;">
            @include('shared._messages')
        </div>
        <!--https://github.com/Lou00/learn_llarveral-->
    @else
    you are not login
    @endif
@stop