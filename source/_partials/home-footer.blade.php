<footer id="footer">
	<ul class="actions">
		<li>
			<a href="{{ $page->home_footer->list[0]->link }}" class="icon {{ $page->home_footer->list[0]->icon }}">
				<span class="label">{{ $page->home_footer->list[0]->title }}</span>
			</a>
		</li>
		<li>
			<a href="{{ $page->home_footer->list[1]->link }}" class="icon {{ $page->home_footer->list[1]->icon }}">
				<span class="label">{{ $page->home_footer->list[1]->title }}</span>
			</a>
		</li>
		<li>
			<a href="{{ $page->home_footer->list[2]->link }}" class="icon {{ $page->home_footer->list[2]->icon }}">
				<span class="label">{{ $page->home_footer->list[2]->title }}</span>
			</a>
		</li>
		<li>
			<a href="{{ $page->home_footer->list[3]->link }}" class="icon {{ $page->home_footer->list[3]->icon }}">
				<span class="label">{{ $page->home_footer->list[3]->title }}</span>
			</a>
		</li>
	</ul>
	<ul class="menu">
		<li>
			{{ $page->home_footer->copyright }}
		</li>
	</ul>
</footer>