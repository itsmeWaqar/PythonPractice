##This is to calculate average 
total = 0
count = 0

while True:
	inp = raw_input('Enter a num:')
	if inp == 'done' : break
	value = float(inp)
	total = total + value
	count = count + 1

average = total/count
print 'Average:', average