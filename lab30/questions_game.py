from datetime import datetime
import time




def process_question(question,correct_answer):
	print(question)
	try:
		response = int(input('Your answer:'))
	except:
		print('The answer is an INTEGER.')
	else:
		if response == correct_answer:
			print('Correct! Keep going.\n')
		else:
			global lives
			lives -= 5
			print(f'Wrong. Current lives: {lives}\n')

def check_lives(lives):
	if lives <= 0:
		print('Sorry, but you are out of lives.')
		print('Exiting the program...\n')
		time.sleep(3)
		quit()
	else:
		pass


if __name__ == '__main__':
	username = input("Enter your username: ")
	lives = 10
	questions = [
		('Q1:  10x - 100 = 20;    x = ', 12 ),
		('Q2:  x^2 = 144;    x = ', 12),
		('Q3:  Sally is 54 years old and her mother is 80, how many years ago was Sally’s mother times her age?;    x = ', 41)
	]

	print(f"Greetings, {username}!")
	print("The goal is to answer 12 questions you are going to be given, spent as little time as possible and save all of your 10 lives!")

	start_time = time.time()

	# for i in range(len(questions)):
	# 	print(questions[i][0])

	for question in questions:
		check_lives(lives)
		process_question(question[0], question[1])


	res_time = time.time() - start_time
	res_time = round(res_time, 2)
	print(f'Congratulations, you passed the test in about {res_time} seconds :)\n')





