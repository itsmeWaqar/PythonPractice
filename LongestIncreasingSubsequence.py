def longest_increasing_subsequence(sequence):
	# Write your solution here
	seq = len(sequence)
	T = [1] * seq
	P = [-1] * seq
	P[1] = -1
	best_index = 1
	for i in range(1,len(sequence)):
		P[i] = -1
		for j in range(i):
			seqI = sequence[i]
			seqJ = sequence[j]
			if sequence[i] > sequence[j] and T[j]+ 1 > T[i]:
				T[i] = max(T[i], T[j] + 1)
				P[i] = j
				if T[best_index] < T[i]:
					best_index = i
	answer = []
	index = best_index
	while index != -1:
		 answer.append(sequence[index])
		 index = P[index]
	answer.reverse()
	return answer

sequence = [16, 3, 5, 19, 10, 14, 12, 0, 15]
answer = longest_increasing_subsequence(sequence)
print answer