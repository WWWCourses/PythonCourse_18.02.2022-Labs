import requests


base_url= 'http://127.0.0.1:8080'


response = requests.get(base_url)

print(response.text)