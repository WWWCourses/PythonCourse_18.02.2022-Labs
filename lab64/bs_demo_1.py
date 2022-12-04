from bs4 import BeautifulSoup

html = """
	<div class="date">
		<span class="sound_icon">dffdsfdds</span>
		<p>Хартиени биогоривни клетки използват ензими за  преобразуване на глюкозата и кислорода в електричество, осигурявайки органично  <b>и компостируемо енергийно решение</b>. Те са органични, икономични, ефективни, без  метал, безопасни и устойчиви.</p>
		<span class="video_icon"></span>
		публикувано на 02.11.22 в 11:55
	</div>
"""

date_div = BeautifulSoup(html,'html.parser')

text = date_div.getText()
print(text)
