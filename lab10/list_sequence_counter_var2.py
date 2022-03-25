""" Напишете програма, която намира максимална редица от последователни
	еднакви елементи в списък.
	Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. ‘2’ * counter
"""

l = [2, 2, 2, 1, 3, 3, 3, 3, 2, 2, 2, 1]

max_sequence_count = 0
current_sequence_count = 0
max_sequence_element = -1


for i in range(len(l)):

	for j in range(i+1,len(l)):
		if l[i]==l[j]:
			current_sequence_count+=1
		else:
			break

	if current_sequence_count>max_sequence_count:
		max_sequence_count = current_sequence_count
		max_sequence_element = l[i]

	current_sequence_count = 0


print( str(max_sequence_element) * max_sequence_count)