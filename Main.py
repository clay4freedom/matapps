from Bin.Prima import mainprog
from Bin.Genap import ganjilgenap
from Bin.Trian import trianprog
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
	print("|[2] Bilangan Ganjil Genap   |")
	print("|[3] Bilangan Segitiga       |")
	print("|[4] Info                    |")
	print("|[5] Exit                    |")
	print("==============================")
	print("==============================")
	choose = int(input("|Input : "))
	print("==============================")
	if choose ==1:
		bilprima()
	elif choose ==2:
		os.system('cls')
		bilgangen()
	elif choose ==5:
		os.system('cls')
		quit()
	elif choose ==4:
		help()
	elif choose ==3:
		bilseg()
	
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
	
def bilgangen():
	os.system('cls')
	print("|============================|")
	print("|  Program Bil. Ganjil Genap |")
	print("|============================|")
	print("|                            |")
	a = int(input("|Masukkan Angka: "))
	print("|============================|")
	ganjilgenap(a)
	input("   Press Enter to Continue!   ")
	
def bilseg():
	os.system('cls')
	print("|============================|")
	print("|   Program Bil. Segitiga    |")
	print("|============================|")
	print("|                            |")
	print("|Masukkan Digit")
	a = int(input("*Ex 3 : "))
	print("|============================|")
	trianprog(a)
	print("|============================|")
	print("Ket:")
	print(">> [1] adalah Digit/Barisnya")
	print()
	print(">> Sebelah kanan adalah hasil")
	print("  dari bilangan segitiga")
	print("|============================|")
	input("   Press Enter to Continue!   ")
	
if __name__ == "__main__":

	while(True):
		main()