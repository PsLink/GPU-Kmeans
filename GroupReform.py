import fileinput

for a in fileinput.input("new.txt"):
	GroupCount = [int(i) for i in a.split()]

newGroupID = [-1]*len(GroupCount)

length = 0
for oldID in range(len(GroupCount)):
	if GroupCount[oldID] > 0:
		newGroupID[oldID] = length
		length += 1

print length

# new groupID
outf = file('group.txt','wb')

for a in fileinput.input("oldgroup.txt"):
	oldG = [int(i) for i in a.split()]

for i in oldG:
	if newGroupID[i] < 0:
		print "wrong"
	outf.write(str(newGroupID[i])+'\n')

outC = file('center.txt','wb')
len = 0
for a in fileinput.input("outCenter.txt"):
	if newGroupID[len] > 0:
		outC.write(a)
	len += 1





