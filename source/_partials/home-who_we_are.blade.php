<section id="who_we_are" class="info main style2 dark fullscreen left" style="background-image:url(images/overlay.png),url(images/{{ $page->who_we_are->picture }} );">
	<div class="content box style2">
		<header>
			<h2>{{ $page->who_we_are->title }}</h2>
		</header>
			<p>
				{{ $page->who_we_are->description }}
			</p>
	</div>
	<a href="{{ $page->who_we_are->buttonlink }}" class="button style2 down anchored">{{ $page->who_we_are->buttontext }}</a>
</section>