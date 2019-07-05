@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Dashboard</div>

                    <div class="card-body">
                        @if (session('status'))
                            <div class="alert alert-success" role="alert">
                                {{ session('status') }}
                            </div>
                        @endif

                        <form method="POST" action="find">
                            @csrf

                            <div class="form-group row">
                                <label for="password"
                                       class="col-md-4 col-form-label text-md-right">{{ __('Username') }}</label>

                                <div class="col-md-6">
                                    <input id="username" type="text"
                                           class="form-control{{ $errors->has('password') ? ' is-invalid' : '' }}"
                                           name="username" required>
                                </div>
                                <button type="submit" class="btn btn-primary">
                                    {{ __('Find') }}
                                </button>
                            </div>

                        </form>
                        <table class="form-control{{ $errors->has('name') ? ' is-invalid' : '' }}" width='100%' border='0' cellspacing='0' cellpadding='0' class='mytable' style='table-layout: fixed'>
                            <tr>
                                <th style="padding-left: 30px;padding-right: 30px" width="%25">{{ __('Id') }}</th>
                                <th style="padding-left: 50px;padding-right: 50px">{{ __('Name') }}</th>
                                <th style="padding-left: 50px;padding-right: 50px">{{ __('Laravel_session') }}</th>
                                <th style="padding-left: 50px;padding-right: 50px">{{ __('Created_at') }}</th>
                            </tr>
                            @if(!empty($id) and !empty($name) and !empty($laravel_session) and !empty($created_at))
                                <tr>
                                    <th style="text-align:center;vertical-align:middle">{{$id}}</th>
                                    <th style="text-align:center;vertical-align:middle">{{$name}}</th>
                                    <th style="word-break:break-all;text-align:center;vertical-align:middle">{{$laravel_session}}</th>
                                    <th style="text-align:center;vertical-align:middle">{{$created_at}}</th>
                                </tr>
                            @endif
                        </table>

                    </div>
                </div>
            </div>
        </div>
    </div>
@endsection
