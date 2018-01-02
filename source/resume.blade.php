@extends('_layouts.master')
@section('head')
@include('_partials.resume-head')
@endsection
@section('body')

@include('_partials.resume-header')

<div class="row main">
<div class="large-6 columns">
@include('_partials.resume-objective')
@include('_partials.resume-specialites')
@include('_partials.resume-computer_skills')
@include('_partials.resume-language_skills')
</div>
<div class="large-6 columns">
@include('_partials.resume-recognitions')
@include('_partials.resume-experience')
@include('_partials.resume-education')
@include('_partials.resume-hobbies_interest')
</div>
</div>

@include('_partials.resume-footer')
@include('_partials.resume-scripts')

@endsection