def tambah(a,b) :
    hasil = a + b 
    return hasil

def kurang(a,b):
    hasil = a - b
    return hasil

def kali(a,b):
    hasil = a * b
    return hasil

def bagi(a,b):
    hasil = a/b
    return hasil

bol = True
print("\n\n----HALLOW SELAMAT DATANG----")
print("\n\na.Penjumlahan \nb.Pengurangan \nc.Perkalian \nd.Pembagian")
while bol == True:
    masukkan = input("\nOperasi apa yang ingin anda lakukan ? (a/b/c/d) : ")
    if masukkan == "a":
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print(f"\nMaka hasilnya adalah : {tambah(a,b)}")
    elif masukkan == "b":
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print(f"\nMaka hasilnya adalah : {kurang(a,b)}")
    elif masukkan == "c":
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print(f"\nMaka hasilnya adalah : {kali(a,b)}")
    elif masukkan == "d":
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print(f"\nMaka hasilnya adalah : {bagi(a,b)}")
    elif masukkan == "Q":
        print('Selesai')
        bol = False
    else:
        print("INPUTAN ANDA TIDAK VALID !!")

        