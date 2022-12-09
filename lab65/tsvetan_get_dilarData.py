from bs4 import BeautifulSoup


html = """<div class="clearfix"></div>
<ul class="dilarData">aaaa
<li>Дата на производство</li><li>#март 2007г.</li>
<li>Тип двигател</li><li>Дизелов</li>
<li>Мощност</li><li>163 к.с.</li>
<li>Евростандарт</li><li>Евро 4</li>
<li>Кубатура [куб.см]</li><li>2000 куб.см</li>
<li>Скоростна кутия</li><li>Автоматична</li>
<li>Категория</li><li>Хечбек</li>
<li>Пробег [км]</li><li>#163000 км</li>
<li>Цвят</li><li>Тъмно сив</li>
</ul>
<div class="clearfix" style="margin-bottom:11px;"></div>"""

soup = BeautifulSoup(html,'html.parser')
dilar_data = soup.find('ul', class_="dilarData")

dilar_data_items = dilar_data.find_all('li')

# print(dilar_data_items[1])
# print(dilar_data_items[15])

date_label = dilar_data.find('li', string='Дата на производство')
print(date_label.next_sibling)








