<div id=header>
<div class=row>
<div class="large-3 columns">
<h2>{{ $page->resume_header->name }}</h2>
<h6 class=light>{{ $page->resume_header->occupation }}</h6></div>
<div class="large-3 columns">
<div class=row>
<div class="small-4 columns light2 italic"><b>Address:</b></div>
<div class="small-8 columns border-left light2 ">
<ul class=no-bullet>
<li>{{ $page->resume_header->address }}</li>
<li>{{ $page->resume_header->city }}</li>
<li>{{ $page->resume_header->country }}</li>
</ul>
</div>
</div>
</div>
<div class="large-3 columns">
<div class=row>
<div class="small-4 columns light2 italic"><b>Contact:</b></div>
<div class="small-8 columns border-left light2">
<ul class=no-bullet>
<li>
	<i class="{{ $page->resume_header->list[0]->icon }}">
		<a href="{{ $page->resume_header->list[0]->link }}">{{ $page->resume_header->list[0]->title }}</a>
	</i>
</li>
<li>
	<i class="{{ $page->resume_header->list[1]->icon }}">
		<a href="{{ $page->resume_header->list[1]->link }}">{{ $page->resume_header->list[1]->title }}</a>
	</i>
</li>
<li>
	<i class="{{ $page->resume_header->list[2]->icon }}">
		<a href="{{ $page->resume_header->list[2]->link }}">{{ $page->resume_header->list[2]->title }}</a>
	</i>
</li>
</ul>
</div>
</div>
</div>
<div class="large-2 columns text-right italic website">
<ul class=no-bullet>
<li>
	<i class="{{ $page->resume_header->list[3]->icon }}">
		<a href="{{ $page->resume_header->list[3]->link }}"> {{ $page->resume_header->list[3]->title }}</a>
	</i>
</li>
</ul>
</div>
</div>
</div>