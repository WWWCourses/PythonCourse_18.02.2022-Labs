# -------------------------------- Задачи 1-7 -------------------------------- #
# class Student():

# 	number_of_students = 0

# 	def __init__(self, name='', course=None, specialisation='', university='', email=None, phone=None):
# 		self.name = name
# 		self.course = course
# 		self.specialisation = specialisation
# 		self.university = university
# 		self.__email = email
# 		self.phone = phone

# 	# getter
# 	@property
# 	def email(self):
# 		return self.__email

# 	#setter
# 	@email.setter
# 	def email(self,x):
# 		if isinstance(x,str):
# 			self.__email = x
# 		else:
# 			raise Exception(f'{x} is not string!')

# 	def get_info(self):
# 		print(f'{self.name} is a student of {self.university} in {self.course}\
# 		 with {self.specialisation}.\nContacts: {self.email}, {self.phone}')

# 	def get_name(self):
# 		print(f'Name of the student is: {self.name}')

# 	def get_specialisation_info(self):
# 		print(f'Course: {self.course} Specialisation: {self.specialisation}, University: {self.university}')

# 	def get_contact(self):
# 		print(f"Student's contact info is phone: {self.phone}, email: {self.email}")


# # pesho = Student('Pesho', 'Java', 'Programing', 'NetIT', 'pesho@abv.bg')

# # print(pesho.email )

# # pesho.email = 5
# # # pesho._Student__email = 5

# # print(pesho.email )


# class TestStudent():

# 	def __init__(self, student):
# 		self.studentClass = student

# 	def test_name(self, name):
# 		test_student = self.studentClass(name)
# 		if name == test_student.name:
# 			print('OK')
# 		else:
# 			print('Error')

# 	test_students = []

# 	@staticmethod
# 	def create_students(studentClass):

# 		TestStudent.test_students.append(studentClass('Gosho', 'Python', 'Programing', 'NetIT', 'python@org.bg', '089888888'))
# 		TestStudent.test_students.append(studentClass('Pesho', 'Java', 'Programing', 'NetIT', 'java@org.bg', '087888888'))
# 		TestStudent.test_students.append(studentClass('Acho', 'JavaScript', 'Programing', 'NetIT', 'jacasvript@org.bg', '089888888'))
# 		TestStudent.test_students.append(studentClass('Spas', 'Ruby', 'Programing', 'NetIT', 'ruby@org.bg', '098888888'))
# 		return TestStudent.test_students

# 	def get_students(self):
# 		for student in self.create_students():
# 			print(student.name)


# # test1 = TestStudent(Student)
# # test1.test_name('Gosho')

# for test_student in TestStudent.create_students(Student):
# 	print(test_student.name)


# # test1.get_students()
# # test1_students = test1.create_students().copy()


# --------------------------------- Задача 11 -------------------------------- #
# Добавете изброим тип BatteryType, който съдържа стойности за тип на
# батерията (Li-Ion, NiMH, NiCd, …) и го използвайте като ново поле за класа Battery.

# from enum import Enum

# BatteryType = {
# 	'LiIon':1,
# 	'NiMH':2,
# 	'NiCd':3
# }

# # class BatteryType(Enum):
# # 	LiIon=1
# # 	NiMH=2
# # 	NiCd=3

# class Battery:
# 	def __init__(self, battery_type) -> None:
# 		self.battery_type = battery_type


# bat1 = Battery(BatteryType['NiMH'])

# print(bat1.battery_type)


# --------------------------- Задача 1 Наследяване --------------------------- #
# n = 3

# for i in range(n):
# 	data = input('Enter data:')
# 	for d in data.split(' '):
# 		print(d)