import requests
import time
import threading

def download_image(url, file_name):
	# get image bytes
	print(f"Start downloading {url}")
	response = requests.get(url)


	if response.ok:
		# write image to file
		with open(file_name, 'wb') as fh:
			fh.write(response.content)
			print(f"File saved to {file_name}")


url = "https://picsum.photos/2400"

start = time.time()
threads  = []

for image_count in range(1,6):
	file_name = f'pic{image_count}.jpg'
	# download_image(url, file_name)
	tr = threading.Thread(target=download_image, args=(url, file_name))
	threads.append(tr)
	tr.start()

for tr in threads:
	tr.join()

end = time.time()

print(f'Total time: {end - start}')

# I/O (Input/Output) Bound =>Threads
# CPU Bound =>Processes






