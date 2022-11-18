import re

html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>mysite.com</title>
</head>
<body>
	<h>
	<ul>
		<li><span>Product 1</span><b>22.5</b></li>
		<li><span>Product 2</span><b>22.5</b></li>
		<li><span>Product 3</span><b>32.5</b></li>
		<li><span>Product 4</span><b>42.5</b></li>
		<li><span>Product 5</span><b>52.5</b></li>
	</ul>
</body>
</html>
"""
rx = re.compile(r'<li><span>(.*?)</span><b>(.*?)</b>')
res = rx.findall(html)
for r in res:
	print(r)


# data = [
# 	['Product 1', 22.5],
# 	['Product 1', 22.5],
# 	['Product 1', 22.5],
# 	['Product 1', 22.5],
# 	['Product 1', 22.5],
# ]



