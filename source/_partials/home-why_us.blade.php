<section id="why_us" class="info main style2 dark fullscreen left" style="background-image:url(images/overlay.png),url(images/{{ $page->why_us->picture }} );">
	<div class="content box style2">
		<header>
			<h2>{{ $page->why_us->title }}</h2>
		</header>
			<p>
				{{ $page->why_us->description }}
			</p>
	</div>
	<a href="{{ $page->why_us->buttonlink }}" class="button style2 down anchored">{{ $page->why_us->buttontext }}</a>
</section>