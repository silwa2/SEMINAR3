# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

while True:

    x = float(input ("Введите точку Х не равную 0: "))
    y = float(input ("Введите точку Y не равную 0: "))

    if (x > 0 and y > 0):
        print ("1 Четверть")
    elif (x < 0 and y > 0):
        print ("2 Четверть")
    elif (x < 0 and y < 0):
        print ("3 Четверть")
    elif (x > 0 and y < 0):
        print ("4 Четверть")
    else:
        print("Вы ввели значение 0 введите заного:")

