<section id="contact" class="main style3 secondary">
	<div class="content">
		<header>
			<h2>{{ $page->contact->title }}</h2>
			<p>{{ $page->contact->description }}</p>
		</header>
		<div class="box">
			<form id="formaction" method="post">			
				<div class="field half first">
					<input type="text" name="name" placeholder="Name" required="required" />
				</div>
				<div class="field half">
					<input type="email" name="email" placeholder="Email" required="required" />
				</div>
				<div class="field">
					<textarea name="message" placeholder="Message" rows="6" required="required"></textarea>
			        <input type="text" name="_gotcha" style="display:none" />
			        <input type="hidden" name="_next" value="thanks" />
				</div>
				<ul class="actions">
					<li><input type="submit" value="Send Message" /></li>
				</ul>
			</form>
		</div>
	</div>
</section>
<script>
    var contactform =  document.getElementById('formaction');
    contactform.setAttribute('action', '//formspree.io/' + '{{ $page->email }}');
</script>