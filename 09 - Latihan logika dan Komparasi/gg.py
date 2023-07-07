angka = 3
if angka % 2 == 0:
    print ("Genap")
else:
    print ("Ganjil")

for i in range(1000):
    if i % 2 == 0:
        print (str(i) + " Adalah Genap")
    else:
        print (str(i) + " Adalah Ganjil")

angka = int(input("Masukkan Angka: "))
if angka % 2 == 0:
    print ("Genap")
else:
    print ("Ganjil")

import time

while True:
    time.sleep(2)
    print ("Merah")
    time.sleep(2)
    print("Hijau")

nilai = "D"

if nilai == "A":
    print ("Lulus")
elif nilai == "B":
    print ("Lulus")
elif nilai == "C":
    print ("Lulus")
elif nilai == "D":
    print ("Ulang")
else:
    print ("DO")

nilai = int(input("Masukkan Nilai"))

if nilai >= 80:
    print ("A")
elif nilai >= 70:
    print ("B")
elif nilai >= 60:
    print ("C")
else:
    print ("D")

r = 8

if r % 7 == 0:
    print (22 / 7 *  r * r)
else:
    print (3.14 * r  * r)

s = 4
print (s * s)

p = float(input("Masukkan Panjang: "))
l = float(input("Masukkan Lebar: "))
print (int(p * l))

while True:
    angka = int(input("Masukkan Angka: "))
    if angka < 10:
        print("Higher")
        continue
    else:
        break

lampu = "kuning"

if lampu == "merah" or lampu == "kuning":
    print ("Berhenti")
elif lampu == "hijau":
    print ("Berangkat")