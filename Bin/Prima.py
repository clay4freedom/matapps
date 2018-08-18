def mainprog(awal, akhir):
	a = awal
	b = akhir
	for i in range (a,b+1):
		prima = True
		for a in range (2,i):
			if i%a ==0:
				prima = False
		if i ==1:
			prima = False
		
		if prima ==True:
			print("|"+str(i),end='| ')