def mainprog(awal, akhir):
	for i in range(awal, akhir+1):
		prima = True
		for j in range(2, (i/2)+1):
			if i % j == 0:
				prima = False
				break
		if prima == True and i != 1:
			print("|" + str(i)+ '| ')