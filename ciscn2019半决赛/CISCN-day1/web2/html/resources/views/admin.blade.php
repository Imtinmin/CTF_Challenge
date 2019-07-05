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

                        @if(empty($online_upload))

                            <form method="POST" action="upload" enctype="multipart/form-data">
                                @csrf

                                <div class="form-group row">
                                    <label for="password"
                                           class="col-md-4 col-form-label text-md-right">{{ __('Upload file') }}</label>

                                    <div class="col-md-6">
                                        <input id="file" type="file"
                                               class="form-control{{ $errors->has('password') ? ' is-invalid' : '' }}"
                                               name="file" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        {{ __('Submit') }}
                                    </button>
                                </div>

                            </form>

                            <a href="online_upload" class="col-md-4 col-form-label text-md-right">{{ __('Upload file online') }}</a>
                            <br>
                            @if(!empty($upload_file) and !empty($hash))
                                <p align="center">{{ __('Upload successful, but deleted! Only empty file can be uploaded. File name is /var/www/html/uploads/'.$hash.'/'.$hash.".jpg") }}<p>
                            @endif
                            @if(!empty($error))
                                <p align="center">{{ $error }}</p>
                            @endif
                        @else
                            <form method="POST" action="online_upload">
                                @csrf

                                <div class="form-group row">
                                    <label for="password"
                                           class="col-md-4 col-form-label text-md-right">{{ __('Picture url') }}</label>

                                    <div class="col-md-6">
                                        <input id="url" type="text"
                                               class="form-control{{ $errors->has('password') ? ' is-invalid' : '' }}"
                                               name="url" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        {{ __('Submit') }}
                                    </button>
                                </div>

                            </form>

                            <a href="index" class="col-md-4 col-form-label text-md-right">{{ __('Upload file') }}</a>
                            <br>
                            @if(!empty($upload_file))
                                <p align="center">{{ __('Upload successful, but deleted! Only empty file can be uploaded. File name is /var/www/html/uploads/'.$hash.'/'.$hash.'.jpg') }}<p>
                            @endif
                            @if(!empty($error))
                                    <p align="center">{{ $error }}</p>
                            @endif
                        @endif
                    </div>
                </div>
            </div>
        </div>
    </div>
@endsection
