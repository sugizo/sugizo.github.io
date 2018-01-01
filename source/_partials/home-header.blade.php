<header id="header">
<h1>
<img alt="{{ $page->title }}" src="images/favicon.png" title="{{ $page->title }}" width="14px">
{{ $page->title }}
</h1>
<nav>
<ul>
<li><a href="{{ $page->header[0]->link }}">{{ $page->header[0]->title }}</a></li>
<li><a href="{{ $page->header[1]->link }}">{{ $page->header[1]->title }}</a></li>
<li><a href="{{ $page->header[2]->link }}">{{ $page->header[2]->title }}</a></li>
<li><a href="{{ $page->header[3]->link }}">{{ $page->header[3]->title }}</a></li>
<li><a href="{{ $page->header[4]->link }}">{{ $page->header[4]->title }}</a></li>
</ul>
</nav>
</header>