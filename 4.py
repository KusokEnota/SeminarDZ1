viruchka = int(input("Введите сумму выручки:"))
izdergka = int(input('Введите  издержки:'))
if viruchka > izdergka:
    profit = viruchka - izdergka
    print("Прибыль - ", profit)
    rent = profit / viruchka
    print("Рентабельность выручки - ", rent)
    chislrab = int(input("введите численность работников фирмы: "))
    sotrprof = profit / chislrab
    print("Прибыль фирмы в расчете на одного сотрудника -", sotrprof)
elif viruchka < izdergka:
    poteri = izdergka - viruchka
    print('Убыток -', poteri)
else:
    print('фин.результат - ноль. Выручка равна издержкам.')
#Задание 4