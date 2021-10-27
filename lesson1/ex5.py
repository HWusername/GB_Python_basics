# 5.

in_vyruchka = int(input("Введите выручку компании: "))
in_izderzki = int(input("Введите издержки компании: "))

v_minus_i = in_vyruchka - in_izderzki

if v_minus_i > 0:
    in_sotrudniki = int(input("Введите численность сотрудников компании: "))
    rentabelnost = v_minus_i / in_vyruchka
    pribyl_na_sotrudnik = v_minus_i / in_sotrudniki
    print("Выручка компании составляет", v_minus_i, "руб.")
    print("Рентабельность компании равна", rentabelnost)
    print("Прибыль компании в расчете на одного сотрудника составляет", pribyl_na_sotrudnik, "руб.")
else:
    print("Убыток компании составляет", v_minus_i, "руб.")
