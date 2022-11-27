import requests

url = 'https://www.mobile.bg/pcgi/mobile.cgi'



def send_request(model):
	data = {
		"act":"3",
		"rub":"1",
		"pubtype":"1",
		"marka":"Audi",
		"bctype":"",
		"topmenu":"1",
		"model":"",
		"bcmarka":"",
		"partrub":"",
		"aksess":"",
		"twrubr":"",
		"location":"",
		"locationc":"",
		"price1":"",
		"year":"",
		"bcgears":"",
		"partelem":"",
		"extinfo":"",
		"sort":"3",
		"engine_t":"",
		"transmis":"",
		"nup":"01"
	}
	headers = {
		"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
		"content-length":"188",
		"content-type": "application/x-www-form-urlencoded"
	}

	r = requests.post(url, data=data, headers=headers)
	print(r)
	if r.ok:
		r.encoding = 'windows-1251'
		return r.text

def get_car_model():
	model = input('Car model:')
	return model

if __name__ =="__main__":
	model = get_car_model()
	html  = send_request(model)

	with open(f'./{model}.html','w') as f:
		f.write(html)