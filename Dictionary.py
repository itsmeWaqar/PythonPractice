#Goes through a file and prints out the max number of emails sent from one email address.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
emailCountDict = {}
for line in fh:
	if line[:5] == 'From ':
		words = line.split()
		emailCountDict[words[1]] = emailCountDict.get(words[1], 0) + 1
MaxKeyValTuple = ('', 0)
for key,val in emailCountDict.items():
	if val > MaxKeyValTuple[1]:
		MaxKeyValTuple = (key, val)
print MaxKeyValTuple[0], MaxKeyValTuple[1]
