from bs4 import BeautifulSoup

html = '''<div class="module mt-20 mb-20 module_listing" id="module_1_1">
	<div class="module_listing_wrapper">
		GET THIS

	</div>
</div>''';

soup = BeautifulSoup(html,'html.parser')

print(dir(soup))






