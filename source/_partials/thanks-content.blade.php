<section class="main style3 secondary">
	<div class="content container">
		<header>
			<h2>{{ $page->thanks->title }}</h2>
		</header>
		<p>{!! $page->thanks->description !!}</p>
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[0]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[1]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[2]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[3]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[4]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[5]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[6]->icon }} fa-stack-1x"></i>
		</span>		
		<span class="fa-stack fa-3x">
			<i class="fa fa-circle-thin fa-stack-2x"></i>
			<i class="fa {{ $page->thanks->list[7]->icon }} fa-stack-1x"></i>
		</span>		
		<div class="12u">
			<ul class="actions">
				<li>
					<a href="/" class="button">{{ $page->thanks->buttontext }}</a>
				</li>
			</ul>
		</div>
	</div>
</section>