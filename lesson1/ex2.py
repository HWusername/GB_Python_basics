# 2.

inp_seconds = int(input("Напишите время в секундах: "))

seconds = inp_seconds % 60
minutes = inp_seconds // 60 % 60
hours = inp_seconds // (60*60) % 24
days = inp_seconds // (60*60*24)

print(f'{days} д. {hours:02}:{minutes:02}:{seconds:02}')
