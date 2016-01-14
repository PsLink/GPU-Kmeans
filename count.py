import fileinput
maxV = 0;
minV = 1000000;
for a in fileinput.input("new.txt"):
	b = a.split()
	c = 0
	for i in b:
		t = int(i)
		if t > 0:
			print t
			c += 1
			if t < minV:
				minV = t
		if t > maxV:
			maxV = t

print c,maxV,minV


