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
### Penjelasan logika dari masing - masing fitur
## Bilangan Prima
### Pengertian :
- adalah suatu bilangan asli yang lebih besar dari angka 1, yang hanya dapat dibagi dengan angka 1 dan bilangan itu sendiri.
### Logikanya :
- Pertama menentukan bilangan awal dan akhir
- for pertama digunaan untuk menentukan range 
- prima = True , baris tersebut menyatakan suatu nilai yang berarti semua nilai dianggap bilangan prima
- for yang kedua digunakan untuk mencari bilangan yang bukan termasuk kriteria bilangan prima ("dapat dibagi selain angka 1 dan dirinya sendiri")
- prima = False , menyatakan bahwa range tersebut bukan bilangan prima
- if i==1:, digunakan untuk menghapus angka 1 dari output
- if prima==True:, digunakan jika nilai prima = True maka tampilkan hasilnya
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
- suatu barisan bilangan yang membentuk sebuah pola bilangan segitiga
### Logikanya :
- Menentukan nilai dari variabel a dan b
- for i in range (2,b+2):, menentukan perulangan agar perulangannya sama dengan nilai dari variabel b
- print digunakan untuk menampilkan hasil dari variabel a
- a+=i, digunakan untuk menjumlahkan variabel a dengan variabel dari perulangan i
- kemudian nilai dari variabel a dan i dijadikan nilai dari variabel a, sehingga nilai dari a selalu berubah selama loop berlangsung.