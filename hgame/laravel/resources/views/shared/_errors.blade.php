@if (count($errors) > 0)
    <div style="color: red">
            @foreach($errors->all() as $error)
                <h5>{{ $error }}</h5>
            @endforeach
    </div>
@endif