def digit_sum(number):
	number = abs(number)
	ls = []
	while number > 0:
		toAdd = number % 10
		ls.append(toAdd)
		number = number /10
	return sum(ls)

num = -1325132435356
print digit_sum(num)
