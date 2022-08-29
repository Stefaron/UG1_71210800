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
while bol == True:
    nilai = (input('Masukkan input :\n'))
    if nilai == 'Q':
        print('Program selesai')
        break
        
    x = nilai.split()
    a = int(x[0])
    b = int(x[2])
    if x[1] == '+':
        print(tambah(a,b))
    elif x[1] == '-':
        print(kurang(a,b))
    elif x[1] == '*':
        print(kali(a,b))
    elif x[1] == '/':
        print(bagi(a,b))
    else:
        print('Inputan anda salah')
