# matapps
---
Simple Mathematics App
---
====Update 17/08/2018====
---
- Menambahkan fitur "bilangan segitiga"
- perubahan readme.md
- Fitur Bilangan genap v2 sementara di hilangkan

---
====Update 15/08/2018====
---
- menambahkan program aplikasi bilangan prima
- menambahkan launcher / program utama
- menambahkan menu info
- menambahkan fungsi main looping

---
====Update 18/08/2018====
---
- mengganti README logika bilangan prima dan bilangan segitiga, serta menambah efisiensi pemrogramannya

---

### Penjelasan logika dari masing - masing fitur
## Bilangan Prima
### Pengertian :
- adalah suatu bilangan asli yang lebih besar dari angka 1, yang hanya dapat dibagi dengan angka 1 dan bilangan itu sendiri.

### Logikanya :
- tentukan bilangan awal dan akhir
- looping: variabel i dari awal sampai bilangan akhir+1 => **range(x,y) dalam python berakhir pada bilangan y-1, karenanya perlu ditambah 1**
	- tandai bilangan tersebut adalah prima dengan variabel prima (**prima=True**)
	- looping: variabel j dari 2 sampai dengan bilangan (i/2)+1
		- jika modulus i/j adalah 0, maka bilangan i adalah kelipatan dari j atau bukan bilangan prima (**prima=False**) dan break (**untuk mempercepat eksekusi**)
	- jika variabel prima berisi **True** dan i bukan bilangan 1, maka itu adalah bilangan prima, maka cetak bilangan tersebut

---
## Bilangan Ganjil Genap
### Pengertian :
#### Bilangan Ganjil
- adalah suatu bilangan bulat dimana bilangan bulat tersebut tidak habis dibagi dengan 2

#### Bilangan Genap
- adalah suatu bilangan bulat dimana bilangan bulat tersebut habis dibagi dengan 2

### Logikanya :
- baris pertama menentukan nilai dari variabel a
- baris kedua digunakan untuk menentukan :
- jika a modulus 2 = 0, maka akan menampilkan hasil bilangan genap
- jika a modulus 2 bukan = 0, maka akan menampilkan hasil bilangan ganjil

---
## Bilangan Segitiga
### Pengertian :
- suatu barisan bilangan yang dapat membentuk sebuah pola segitiga

### Logikanya :
- tentukan jumlah digit bilangan segitiga yang diinginkan
- tentukan digin ke-0 bilangan segitiga (**variable i**) adalah 0
- looping: variable j dari 1 sampai dengan digit yang diinginkan + 1 => **range(x,y) dalam python berakhir pada bilangan y-1, karenanya perlu ditambah 1**
	- tambahkan bilangan segitiga (**variabel i**) dengan digit saat itu (**i +=j**)
	- cetak bilangan segitiga pada digit ke-j adalah i
