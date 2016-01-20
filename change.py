import fileinput

hTable = 6

maxV = [0]*hTable
threshold = [0]*hTable
count = []
for i in xrange(hTable):
	count.append([0]*10000)
	


for line in fileinput.input("datalsh.txt"):
	i = 0
	for tmp in line.split():
		ID = int(tmp)
		count[i][ID] = count[i][ID] + 1
		if ID > maxV[i]:
			maxV[i] = ID
		i = i+1

newLSH = []
for i in xrange(hTable):
	newLSH.append([0]*(maxV[i]+1))


for i in xrange(hTable):
	sum = 0
	t = maxV[i]/3*2
	for j in xrange(t):
		sum = sum + count[i][j]
	threshold[i] = sum/(t)

	
	tmp = count[i][0]
	newLSH[i][0] = 0

	for j in xrange(1,maxV[i]+1):
		tmp = tmp + count[i][j]
		if tmp > threshold[i]:
			tmp = count[i][j]
			newLSH[i][j] = newLSH[i][j-1]+1
		else:
			newLSH[i][j] = newLSH[i][j-1]
			count[i][j] = count[i][j-1] + count[i][j]
			count[i][j-1] = 0

outf1 = file('data_lsh.txt','wb')
for line in fileinput.input("datalsh.txt"):
	i = 0
	for tmp in line.split():
		ID = int(tmp)
		outf1.write(str(newLSH[i][ID])+' ')
		i = i+1
	outf1.write("\n")

outf2 = file('query_lsh.txt','wb')
for line in fileinput.input("querylsh.txt"):
	i = 0
	for tmp in line.split():
		ID = int(tmp)
		outf2.write(str(newLSH[i][ID])+' ')
		i = i+1
	outf2.write("\n")


# for i in xrange(hTable):
# 	print "====================",i,"===================="
# 	for j in range(10000):
# 		if count[i][j] > 0 :
# 			print j,'\t',count[i][j]
