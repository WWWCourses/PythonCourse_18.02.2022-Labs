from bs4 import BeautifulSoup
import re

# TASK: get links and title of each ".module_listing_wrapper", if year >2010
html = '''
<body>
	<h1>Page Title</h1>
	<div class="module mt-20 mb-20 module_listing" id="films">
		<div class="film">
				<a href="/title/tt9114286" title="Ryan Coogler">Black Panther:</a>
				<span class="secondaryInfo">(2009)</span>
				<div class="velocity">1(no change)</div>
		</div>
		<div class="film">
			<a href="/title/tt9114254" title="Letitia Wright" class="red blue">Wakanda Forever</a>
			<span class="secondaryInfo">(2022)</span>
			<div class="velocity">1(no change)</div>
		</div>
	</div>
	<hr>
	<div class="something>
		<div class="film">
			<a href="/title/tt9114254" title="Letitia Wright">Wakanda Forever</a>
			<span class="secondaryInfo">(2022)</span>
			<div class="velocity">1(no change)</div>
		</div>
	</div>
</body>
''';


soup = BeautifulSoup(html,'html.parser')
data = list()

# get all ".film" div which are child of div(id="module_1_1")
films_div=soup.find(id='films')

film_divs = films_div.find_all('div', class_='film')
for div in film_divs:
	year = div.span.string

	rx = re.compile(r'(\d+)')
	m =rx.search(year)
	if m:
		year = int(m.group(1))

	if year>2010:
		a = div.a
		print(a.attrs)
		data.append(a.attrs)



