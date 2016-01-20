# Check if the grouping is correct

import fileinput
for a in fileinput.input("group.txt"):
	b = a.split()
	print len(b)

