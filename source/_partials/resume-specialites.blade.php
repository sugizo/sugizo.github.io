<div class=avoid_pagebreak>
<h4>{{ $page->specialities->title }}</h4>
<ul class="inline-list special first last">
<li class="animated {{ $page->specialities->list[0]->animated }}">
	<i class="{{ $page->specialities->list[0]->icon }}"></i>
<div class="pointer hide-for-small-only "></div>
<div class=desc>{{ $page->specialities->list[0]->title }}</div>
</li>
<li class="animated {{ $page->specialities->list[1]->animated }}">
	<i class="{{ $page->specialities->list[1]->icon }}"></i>
<div class="pointer hide-for-small-only second"></div>
<div class=desc>{{ $page->specialities->list[1]->title }}</div>
</li>
<li class="animated {{ $page->specialities->list[2]->animated }}">
	<i class="{{ $page->specialities->list[2]->icon }}"></i>
<div class="pointer hide-for-small-only "></div>
<div class=desc>{{ $page->specialities->list[2]->title }}</div>
</li>
</ul>
</div>