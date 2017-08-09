def getListofIntByDigit(number):
	number = abs(number)
	ls = []
	while number > 0:
		ls.append(number % 10)
		number = number / 10
	return ls

def is_numeric_palindrome(num):
	ls = getListofIntByDigit(num)
	for i in range(len(ls)/2):
		if ls[i] != ls[len(ls) - i - 1]:
			return False
	return True
print is_numeric_palindrome(123)