import requests

# --------------------------------- example 1 -------------------------------- #
# base_url = 'https://httpbin.org/get'
# base_url = 'https://api.chucknorris.io/jokes/random'

# headers={
# 	'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
# }

# params = {
# 	'id':1
# }
# response = requests.get(base_url, params=params)

# # print(response.status_code)

# if response.ok:
# 	# print(response.text)
# 	# print(type(response.json()))

# 	data = response.json()
# 	print(data['value'])


# --------------------------------- example 2 -------------------------------- #

# requests.get() send the request and returns a Response Object:
# response = requests.get('https://httpbin.org/get')

# ### We can access the request object from the response as:
# # print(response.request)

# # Let's see the default headers sent:
# print(response.request.headers)
# print('headers as seen from server')
# print(response.text)



# ------------------------------- post request ------------------------------- #
# base url
# url = 'http://127.0.0.1:8000/'

# # prepare headers
# headers = {
#   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
# }

# data = {
#   'username':'python_course_test',
#   'password':'python_course_test123'
# }

# # send request
# response = requests.post(url, headers=headers, data=data)

# if response.ok:
#   # print(response.text)
#   with open('./res.html','w') as f:
#     f.write(response.text)