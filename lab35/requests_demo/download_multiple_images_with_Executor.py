import requests
import time
import concurrent.futures

def download_image(url, file_name):
	# get image bytes
	print(f"Start downloading {url}")
	response = requests.get(url)


	if response.ok:
		# write image to file
		with open(file_name, 'wb') as fh:
			fh.write(response.content)
			print(f"File saved to {file_name}")

download_count = 5
urls = ["https://picsum.photos/2400"] * download_count
file_names = list()
for i in range(1, download_count+1):
	file_names.append(f'img{i}.jpg')

if __name__ == "__main__":
  start= time.perf_counter()

  with concurrent.futures.ThreadPoolExecutor() as executor:
	# TODO: make it work
    executor.map(download_image, (urls,file_names))
    executor.shutdown(wait=True)

  end = time.perf_counter()

  print(f'Total time: {end - start}')

# I/O (Input/Output) Bound =>Threads
# CPU Bound =>Processes






