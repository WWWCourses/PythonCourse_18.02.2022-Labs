import time
import asyncio

async def async_sleep():
	print('Do something')
	await asyncio.sleep(1)


#sync (blocking) sleep
print('Sync sleep start')
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)

# TODO: make example works and add it to PP_Lecture_5
print('Async sleep start')
# async (non-blocking) sleep
print(1)
asyncio.run(async_sleep())
print(2)
asyncio.run(async_sleep())
print(3)