<div class=avoid_pagebreak>
<h4>{{ $page->language_skills->title }}</h4>
<div class="row lang">
<div class="large-4 medium-4 small-6 columns">
<ul data-pie-id=lang1 class=pie_desc data-options='{"donut_inner_ratio":"0.8"}'>
<li data-value=100>
<div class=lang_info>
	<span class=lang_name>{{ $page->language_skills->list[0]->title }}</span>
	<span class=lang_level>{{ $page->language_skills->list[0]->level }}</span>
</div>
</li>
</ul>
<div id=lang1 class="pie nostroke animated bounceIn"></div>
</div>
<div class="large-4 medium-4 small-6 columns">
<ul data-pie-id=lang2 class=pie_desc>
<li data-value=75>
<div class=lang_info>
	<span class=lang_name>{{ $page->language_skills->list[1]->title }}</span>
	<span class=lang_level>{{ $page->language_skills->list[1]->level }}</span>
</div>
</li>
<li data-value=25></li>
</ul>
<div id=lang2 class="pie  animated bounceIn"></div>
</div>
<div class="large-4 medium-4 small-6 columns">
<ul data-pie-id=lang3 class=pie_desc>
<li data-value=50>
<div class=lang_info>
	<span class=lang_name>{{ $page->language_skills->list[2]->title }}</span>
	<span class=lang_level>{{ $page->language_skills->list[2]->level }}</span>
</div>
</li>
<li data-value=50></li>
</ul>
<div id=lang3 class="pie  animated bounceIn"></div>
</div>
</div>
</div>