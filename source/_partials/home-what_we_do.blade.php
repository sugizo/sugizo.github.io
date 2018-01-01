<section id="what_we_do" class="info main style2 dark fullscreen right" style="background-image:url(images/overlay.png),url(images/{{ $page->what_we_do->picture }} );">
	<div class="content box style2">
		<header>
			<h2>{{ $page->what_we_do->title }}</h2>
		</header>
			<p>
				{{ $page->what_we_do->description }}
			</p>
	</div>
	<a href="{{ $page->what_we_do->buttonlink }}" class="button style2 down anchored">{{ $page->what_we_do->buttontext }}</a>
</section>