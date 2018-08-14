from Prima import mainprog
import os
os.system("mode con cols=30 lines=40")
def main():
	print("==============================")
	print("|                            |")
	print("|======Mathematics Apps======|")
	print("|                            |")
	print("==============================")
	print("|==========M E N U===========|")
	print("==============================")
	print("|[1] Bilangan Prima          |")
	print("|[2] Bilangan Genap          |")
	print("|[3] Bilangan Genap v2       |")
	print("|[4] Bilangan Ganjil         |")
	print("|[5] Bilangan Ganjil v2      |")
	print("|[6] Info                    |")
	print("|[7] Exit                    |")
	print("==============================")
	print("==============================")
	choose = int(input("|Input : "))
	print("==============================")
	if choose ==1:
		bilprima()
	elif choose ==7:
		exit
	
def bilprima():
	os.system('cls')
	print("|============================|")
	print("|==|Program Bilangan Prima|==|")
	print("|============================|")
	print()
	a = int(input("Masukkan Nilai Awal : "))
	b = int(input("Masukkan Nilai Akhir: "))
	print()
	print("|============================|")
	print("|============================|")
	print("|=========[Hasilnya]=========|")
	print()
	mainprog(a,b)
	print()
	print()
	print("|============================|")
	
main()