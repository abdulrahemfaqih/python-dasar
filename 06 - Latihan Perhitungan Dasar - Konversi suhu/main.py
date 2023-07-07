# latihan konversi satuan suhu

print("\nPROGRAM KONVERSI UANG\n")

# CELCIUS
celcius = float(input('masukkan suhu dalam celcius :'))
print("\nsuhu adalah", celcius, "celcius\n")

# REAMUR -----> 4/5*C
reamur = (4/5) * celcius
print("\nsuhu dalam reamur adalah", reamur, "reamur\n")


# FAHRENHEIT ------> 9/5*C + 32
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit\n")


# KELVIN ------->
kelvin = celcius + 273
print("/nsuhu dalam kelvin adalah", kelvin, "kelvin\n")
