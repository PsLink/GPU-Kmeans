# Calculate the radius of each group.

import math
import fileinput
maxPoint = 1000000
dimension = 128
i = 0
gID = []
center = []
radius = []
count = []

def dis(a,b):
        length = dimension
        d = 0
        for i in range(length):
                x = a[i]
                y = b[i]
                d += (x-y)*(x-y)
        return d


for tmp in fileinput.input("group.txt"):
        l = tmp.split()
        for j in l:
                gID.append(int(j))
# print gID

for tmp in fileinput.input("outCenter.txt"):
        l = tmp.split()
        t = []
        for j in l:
                t.append(float(j))
        center.append(t)
        radius.append(0)
        # print t

length = len(radius)

count = [0]*length
sumR = [0]*length
minR = [250000]*length

#print center
i = 0
for tmp in fileinput.input("oData.txt"):
        l = tmp.split()
        point = []
        for j in l:
                point.append(int(j))
        tmpDis = dis(point,center[gID[i]])
        if tmpDis>radius[gID[i]]:
                radius[gID[i]] = tmpDis
        if tmpDis<minR[gID[i]]:
                minR[gID[i]] = tmpDis    
        sumR[gID[i]] += math.sqrt(tmpDis)
        count[gID[i]] += 1  
        i += 1
        if i == maxPoint:
                break

for i in range(length):
	radius[i] = math.sqrt(radius[i])
        minR[i] = math.sqrt(minR[i])

for i in range(length):
        if count[i]>0:
                print minR[i],'\t',radius[i],'\t',sumR[i]/count[i],'\t',count[i]


