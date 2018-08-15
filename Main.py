from Prima import mainprog
from Info import infoprog
import os

os.system("mode con cols=30 lines=40")

def main():
	os.system('cls')
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
		os.system('cls')
		quit()
	elif choose ==6:
		help()
	
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
	input("   Press Enter to Continue!   ")
	
def help():
	os.system('cls')
	print("|============================|")
	print("|                            |")
	print("|========Program Info========|")
	print("|                            |")
	infoprog()
	input("   Press Enter to Continue!   ")
	
if __name__ == "__main__":

	while(True):
		main()