from random import randint
number_1 = 18
print(number_1)
result = ''
for i in range(1, 20):
	for w in range(1, 20):
		if number_1 % (i + w) == 0 and i < w:
			result += (str(i) + str(w))
			# print(f'{i} + {w}')

print(result)