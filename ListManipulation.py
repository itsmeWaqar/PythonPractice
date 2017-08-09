
while True:
	fileName = raw_input("Enter the file name:")
	try:
		fh = open(fileName)
		break
	except:
		print 'FIle Not found'
fh = open(fileName)

for line in fh:
	print line[:4]



