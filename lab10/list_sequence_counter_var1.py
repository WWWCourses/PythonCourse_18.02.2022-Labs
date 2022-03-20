""" Напишете програма, която намира максимална редица от последователни
	еднакви елементи в списък.
	Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. ‘2’ * counter
"""

l = [2, 3, 3, 1, 1, 2, 3, 3, 2, 2, 2, 1]

sequence_value = 0
sequence_counter = 0
sequence_counter_tmp = 0

for i in l:
	sequence_counter_tmp = 0
	# check if next elements == i:
	for j in l:
		if i==j:
			sequence_counter_tmp+=1
		else:
			break

	if sequence_counter_tmp>sequence_counter:
		sequence_counter = sequence_counter_tmp
		sequence_value = j


print(f'sequence_value: {sequence_value}')
print(f'sequence_counter: {sequence_counter}')
print(f'sequence_counter_tmp: {sequence_counter_tmp}')



