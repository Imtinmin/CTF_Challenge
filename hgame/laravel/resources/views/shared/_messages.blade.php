@foreach (['danger',  'success','info'] as $msg)
    @if(session()->has($msg))
        @if($msg === 'success')
            <div style="color:green;">
                <p class="alert alert-{{ $msg }}">
                    {{ session()->get($msg) }}
                </p>
            </div>
        @elseif($msg === 'danger')
            <div style="color:red;">
                <p class="alert alert-{{ $msg }}">
                    {{ session()->get($msg) }}
                </p>
            </div>
        @else
            <div>
                <p class="alert alert-{{ $msg }}">
                    {{ session()->get($msg) }}
                </p>
            </div>
        @endif
    @endif
@endforeach