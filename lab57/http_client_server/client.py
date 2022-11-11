import requests


base_url= 'http://127.0.0.1:8080'


def make_get_req():
	response = requests.get(base_url)
	print(response.text)

def send_user_data():
	user_name = 'Ada'
	user_pass = '123'

	headers = {
		'user-agent':'Chrome'
	}

	response = requests.post(
		base_url,
		data = {'userName':user_name,'userPass':user_pass},
		headers=headers
	)

	# userName=Ada&userPass=123

# send_user_data()
make_get_req()
