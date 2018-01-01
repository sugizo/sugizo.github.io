<section id="intro" class="main style1 dark fullscreen" style="background-image:url(images/overlay.png),url(images/{{ $page->intro->picture }} );">
	<div class="content">
		<header>
			<h2>{{ $page->intro->title }}</h2>
		</header>
			<p>
				{{ $page->intro->description }}
			</p>
		<footer>
			<a href="{{ $page->intro->buttonlink }}" class="button style2 down">{{ $page->intro->buttontext }}</a>
		</footer>
	</div>
</section>