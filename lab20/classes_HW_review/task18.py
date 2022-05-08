# Задача 18. В класа GSM добавете метод, който пресмята общата сума на обажданията
# (Call) от архива с обаждания на телефона (callHistory) като нека цената за едно обаждане
# се подава като параметър на метода.

class Call:
	callHistory = list()

	def __init__(self, date, time, duration):
		self.date = date
		self.time = time
		self.duration = duration
		callData = list()
		callData.append(date)
		callData.append(time)
		callData.append(duration)

		Call.callHistory.append(callData)


class GSM:
	price = 0

	def __init__(self, model="", manufacturer="", price=0, owner=""):
		self.model = model
		self.manufacturer = manufacturer
		self.price = price
		self.owner = owner

	def total_price(price_min):
		total_duration = 0
		# [ ['14.04.2022', '15:30', 14], ['15.04.2022', '18:10', 25]]
		for el in Call.callHistory:
			total_duration += int(el[2])
		GSM.price = total_duration * int(price_min)
		print(GSM.price)


call1 = Call("14.04.2022", "15:30", 10)
call2 = Call("15.04.2022", "18:10", 20)

GSM.total_price(2)
