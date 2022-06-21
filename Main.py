# ------------------------Loop------------------------
for i in range(2 * 10):
	print(i)


for i in range(2 , 5):
	print('Hello' * i)


list = ['a','b','c','d']

for i in range(len(list)):
	print(list[i])

for i in range(2, len(list)):
	print(list[i])

for i in range(2, len(list)-1):
	list[i] *= i
	print(list)

for j in range(10, 5, -1):
	print(j)

for i in range(len(list)-1, 1, -1):
	print(list[i])
