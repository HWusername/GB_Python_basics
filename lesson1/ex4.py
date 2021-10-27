# 4.

inp_num = int(input("Введите любое целое положительное число: "))
ostatok = inp_num % 10
inp_num_mod = inp_num // 10
while inp_num_mod > 0:
    if ostatok > inp_num_mod % 10:
        max_num = ostatok
        inp_num_mod = inp_num_mod // 10
    else:
        ostatok = inp_num_mod % 10
        max_num = ostatok
        inp_num_mod = inp_num_mod // 10
print(max_num)