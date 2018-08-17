def trianprog(digit):
	a = 1
	b = digit
	for i in range (2,b+2):
		print ("["+str(i-1)+"]",a)
		a = a + i