isim = input("isminizi yazın")
soyad = input("soyadınızı yazın")
print(isim, soyad)

x = 7
y = 77
print(x + y)
print(x - y)
print(x * y)

yas = int(input("yaş girin"))
print(yas>18)

a = int(input("kısa kenar:"))
b = int(input("uzun kenarını gir"))
alan = a * b
cevre = 2 * (a + b)
print("alan:", alan)
print("çevre:", cevre)

sayı = int(input("bir sayı girin:"))
print("pozitif mi?", sayı > 0)

kelime = input("Bir kelime girin:")
print("ilk 3 harf:", kelime[:3])
print("son 2 harf:", kelime[-2])

a = float(input("1.sayıyı giriniz:"))
b = float(input("ikinci sayıyı giriniz:"))
sonuc = (a + b) / 2
print("sonuç:", sonuc)

a= int(input("1. sayıyı giriniz:"))
b = int(input("2. sayıyı giriniz:"))
print(a % 2 == 0 and b % 2 == 0)

metin = input("bir metin giriniz:")
print("uzunluk:", len(metin))
print("büyük harf hali:", metin.upper())



pi = 3
r = float(input("yarıçap girin"))

alan = pi * (r ** 2)
print("ALAN:", alan)

a = int(input("1. sayıyı giriniz:"))
b = int(input("2 sayıyı giriniz"))
print("eşit mi:", a == b)
print("birinci büyük mü:", a > b)

sayi = int(input("sayı girin:"))
print(sayi % 3 == 0 and sayi % 5 == 0)