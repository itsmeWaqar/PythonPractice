def jump_over_numbers(ls):
	pos = 0
	ans = 0
	length = len(ls)
	while pos < length:
		if ls[pos] == 0:
			return -1
		ans += 1
		pos += ls[pos]
	return ans

ls = [0, 0, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]
print jump_over_numbers(ls)