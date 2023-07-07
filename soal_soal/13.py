import os
os.system('cls')


day = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
print(day)
# hari ini = 2
# Hari kemudian = 3
# hari ini + hari kemudian = 5
now = int(input('\nhari ini = '))
tomorrow = int(input('hari kemudian = '))

print(f'\nhari ini = {day[now % 7]}')
print(f'hari kemudian = {day[tomorrow % 7]}\n')
print(f'hari ini + hari kemudian = {now + tomorrow} --> {day[(now + tomorrow) % 7]}\n')

