#read romeo.txt line by line.
while True:
	fileName = raw_input("Enter the file name:")
	try:
		fh = open(fileName)
		break
	except:
		print 'FIle Not found'
fh = open(fileName)
count = 0
for line in fh:
	if line[:5] == 'From ':
		line = line.rstrip()
		words = line.split()
		print words[1]
		count = count+1
print 'There were', count, 'lines in the file with From as the first word'


