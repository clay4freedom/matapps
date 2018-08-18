def trianprog(digit):
	i = 0
	for j in range (1, digit+1):
		i += j
		print ("[" + str(j) + "]", i)