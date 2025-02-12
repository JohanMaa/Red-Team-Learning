# Panduan Dasar Python

## 1. Menampilkan Teks ke Layar

Untuk memulai, kita akan membuat program sederhana yang menampilkan teks ke layar.

```python
# Ini adalah contoh komentar
print("Hello World")
```

Pada contoh di atas:
- **Baris 1** adalah komentar yang diawali dengan tanda pagar (`#`). Komentar tidak dijalankan oleh komputer, tetapi digunakan oleh programmer untuk memberikan penjelasan dalam kode.
- **Baris 2** menggunakan perintah `print()` untuk mencetak teks ke layar.
- Teks yang ingin ditampilkan harus ditulis di dalam tanda **kutip dua (")** karena merupakan **string**.

---

## 2. Operator Matematika dalam Python

Seperti kalkulator, Python dapat melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian. Berikut tabel operator yang digunakan:

| **Operator** | **Simbol** | **Contoh** |
|-------------|-----------|------------|
| Penjumlahan | `+` | `1 + 1 = 2` |
| Pengurangan | `-` | `5 - 1 = 4` |
| Perkalian | `*` | `10 * 10 = 100` |
| Pembagian | `/` | `10 / 2 = 5` |
| Modulus (Sisa hasil bagi) | `%` | `10 % 2 = 0` |
| Pangkat (Eksponen) | `**` | `5**2 = 25` |

---

## 3. Operator Perbandingan

Operator ini digunakan untuk membandingkan dua nilai dalam program dan sering digunakan dalam **kondisi** (seperti pernyataan `if`).

| **Simbol** | **Fungsi** |
|------------|------------|
| `>` | Lebih besar dari |
| `<` | Lebih kecil dari |
| `==` | Sama dengan |
| `!=` | Tidak sama dengan |
| `>=` | Lebih besar atau sama dengan |
| `<=` | Lebih kecil atau sama dengan |

---

## 4. Operator Logika

Operator logika digunakan dalam pengujian kondisi (seperti dalam `if` statement).

| **Operasi Logika** | **Operator** | **Contoh** |
|-----------------|------------|-----------|
| Kesetaraan | `==` | `if x == 5` |
| Kurang dari | `<` | `if x < 5` |
| Kurang dari atau sama dengan | `<=` | `if x <= 5` |
| Lebih besar dari | `>` | `if x > 5` |
| Lebih besar atau sama dengan | `>=` | `if x >= 5` |

### **Operator Boolean**
Operator boolean digunakan untuk menghubungkan atau membandingkan hubungan antara pernyataan.

| **Operasi Boolean** | **Operator** | **Contoh** |
|-----------------|------------|-----------|
| Kedua kondisi harus benar agar pernyataan bernilai benar | `AND` | `if x >= 5 AND x <= 100` |
| Salah satu kondisi cukup untuk membuat pernyataan benar | `OR` | `if x == 1 OR x == 10` |
| Mengembalikan kebalikan dari kondisi | `NOT` | `if NOT y` |

### **Contoh Penggunaan**

```python
a = 1
if a == 1 or a > 10:
     print("a adalah 1 atau lebih besar dari 10")

name = "bob" 
hungry = True
if name == "bob" and hungry == True:
     print("Bob sedang lapar")
elif name == "bob" and not hungry:
     print("Bob tidak lapar")
else:
     print("Tidak yakin siapa ini atau apakah dia lapar")
```

---

## 5. Variabel dalam Python

Variabel digunakan untuk menyimpan dan memperbarui data dalam program.

```python
food = "ice cream"
money = 2000
```

Pada contoh di atas:
- **Variabel `food`** menyimpan nilai berupa teks `"ice cream"`.
- **Variabel `money`** menyimpan angka `2000`.

Variabel bisa diubah nilainya dalam program.

```python
age = 30
age = age + 1
print(age)
```
- Pada baris kedua, nilai **`age`** yang awalnya `30` diperbarui dengan menambahkan `1`, sehingga hasil akhirnya adalah `31`.

---

## 6. Tipe Data dalam Python

| **Tipe Data** | **Penjelasan** |
|--------------|---------------|
| **String** | Digunakan untuk teks atau kombinasi karakter (huruf, simbol, angka) |
| **Integer** | Bilangan bulat (tanpa desimal) |
| **Float** | Bilangan dengan desimal (misalnya untuk pecahan) |
| **Boolean** | Menyimpan nilai **True** atau **False** |
| **List** | Kumpulan berbagai tipe data yang disimpan dalam satu variabel |

![image](https://github.com/user-attachments/assets/23778cc1-b666-4e59-9863-f1cc51ad122f)

---

## 7. Penggunaan `if` Statement

Menggunakan `if statement` memungkinkan program untuk membuat keputusan berdasarkan suatu kondisi.

```python
if age < 17:
    print('Kamu BELUM cukup umur untuk mengemudi')
else:
    print('Kamu cukup umur untuk mengemudi')
```

Pada contoh di atas:
- Jika usia kurang dari `17`, program akan mencetak `"Kamu BELUM cukup umur untuk mengemudi"`.
- Jika usia `17` atau lebih, program akan mencetak `"Kamu cukup umur untuk mengemudi"`.

### **Komponen Penting dalam `if` Statement**
1. Kata kunci **`if`** diikuti oleh kondisi.
2. Jika kondisi bernilai **True**, kode dalam `if` akan dijalankan.
3. **`else`** digunakan untuk menangani kondisi jika `if` tidak terpenuhi.
4. Tanda **`:`** menandakan akhir dari kondisi `if`.
5. Indentasi sangat penting! Kode yang berada di dalam `if` harus diberi indentasi agar dikenali sebagai bagian dari blok `if`.

![image](https://github.com/user-attachments/assets/43958c08-525c-4578-ae8d-42b6b95a8b58)


`if` statement sangat penting dalam pemrograman dan akan sering digunakan.

---


## 8. Perulangan dalam Python

Dalam pemrograman, perulangan memungkinkan program untuk mengulang dan menjalankan aksi beberapa kali. Ada dua jenis perulangan, yaitu perulangan `for` dan `while`.

### Perulangan While

Mari kita mulai dengan melihat bagaimana kita menyusun perulangan `while`. Kita dapat membuat perulangan berjalan tanpa batas atau (mirip dengan pernyataan `if`) menentukan berapa kali perulangan harus dijalankan berdasarkan suatu kondisi.

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

Perulangan `while` ini akan berjalan 10 kali, menampilkan nilai variabel `i` setiap kali iterasi (pengulangan). Mari kita bahas lebih lanjut:

- Variabel `i` disetel ke 1.
- Pernyataan `while` menentukan awal perulangan.
- Setiap kali perulangan berjalan, ia akan mulai dari atas (menampilkan nilai `i`).
- Kemudian program berpindah ke baris berikutnya dalam perulangan, yang meningkatkan nilai `i` sebesar 1.
- Setelah tidak ada kode lagi untuk dieksekusi, program kembali ke awal perulangan dan mengulang prosesnya.
- Program akan terus berulang hingga nilai `i` lebih besar dari 10.

### Perulangan For

Perulangan `for` digunakan untuk mengiterasi suatu urutan seperti daftar (`list`). Daftar digunakan untuk menyimpan banyak item dalam satu variabel dan dibuat menggunakan tanda kurung siku (`[]`). Mari kita lihat contoh berikut:

```python
websites = ["facebook.com", "google.com", "amazon.com"]
for site in websites:
    print(site)
```

Perulangan `for` dalam kode di atas akan berjalan 3 kali, menampilkan setiap situs web dalam daftar. Penjelasannya:

- Variabel `websites` menyimpan 3 elemen.
- Perulangan mengiterasi setiap elemen, mencetak elemen tersebut.
- Program berhenti setelah semua elemen dalam daftar telah diproses.

Untuk contoh di dunia nyata, Anda dapat membuat program yang memeriksa apakah sebuah situs web online atau apakah suatu item tersedia dalam stok. Anda akan mengiterasi daftar situs web, menambahkan fungsionalitas dalam perulangan untuk memeriksa situs tersebut, dan menampilkan hasilnya.

Python juga memungkinkan iterasi melalui rentang angka menggunakan fungsi `range()`. Berikut contoh kode Python yang akan mencetak angka dari 0 hingga 4:

```python
for i in range(5):
    print(i)
```

## 9. Fungsi dalam Python

Seiring bertambahnya ukuran dan kompleksitas program, beberapa kode akan menjadi repetitif. Inilah saatnya kita menggunakan fungsi. Fungsi adalah blok kode yang dapat dipanggil di berbagai tempat dalam program.

Contoh fungsi sederhana:

```python
def sayHello(name):
    print("Hello " + name + "! Nice to meet you.")

sayHello("Ben")  # Output: Hello Ben! Nice to meet you.
```

Komponen utama dalam fungsi ini:

- Kata kunci `def` menandai awal fungsi.
- Nama fungsi ditentukan oleh programmer (contohnya `sayHello`).
- Tanda kurung `()` berisi parameter yang dapat diberikan ke fungsi (contohnya `name`).
- Tanda `:` mengakhiri deklarasi fungsi.
- Indentasi setelah `:` menunjukkan blok kode fungsi.

Fungsi juga bisa mengembalikan hasil dengan `return`, contoh:

```python
def calcCost(item):
    if item == "sweets":
        return 3.99
    elif item == "oranges":
        return 1.99
    else:
        return 0.99

spent = 10
spent = spent + calcCost("sweets")
print("You have spent:" + str(spent))
```

Jika kita memanggil `calcCost("sweets")`, fungsi akan mengembalikan nilai `3.99`, yang kemudian ditambahkan ke variabel `spent`.

## 10. Membaca dan Menulis File dalam Python

Python memungkinkan kita membaca dan menulis file. Contoh membaca file:

```python
f = open("file_name", "r")
print(f.read())
```

`open("file_name", "r")` membuka file dalam mode baca (`r`). Metode `read()` digunakan untuk membaca isi file.

Untuk menulis ke file, gunakan mode `a` (append) atau `w` (write):

```python
f = open("demofile1.txt", "a")  # Menambahkan ke file
f.write("Menambahkan teks baru..")
f.close()

f = open("demofile2.txt", "w")  # Membuat file baru
f.write("File baru dibuat!")
f.close()
```

Gunakan `close()` setelah menulis agar file tertutup dan tidak dapat ditulis lagi.

## 11. Menggunakan Library dalam Python

Python memiliki berbagai library yang dapat diimpor untuk memperluas fungsionalitas. Contoh penggunaan library `datetime`:

```python
import datetime
current_time = datetime.datetime.now()
print(current_time)
```

Beberapa library populer untuk pentesting:

- `requests` - library HTTP sederhana.
- `scapy` - mengirim, mengendus, membedah, dan memalsukan paket jaringan.
- `pwntools` - library untuk CTF & exploit development.

Jika library belum terinstal, gunakan `pip` untuk menginstalnya:

```sh
pip install scapy
```

Setelah diinstal, library bisa langsung diimpor dan digunakan dalam program Python Anda.

---

