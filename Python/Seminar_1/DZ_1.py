# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

while True:
    day = int (input("Введите день недели: "))
    if day == 6 or day == 7:
        print ("ДА\n")
    elif day<1 or day>7:
        print("Такого дня недели не существует!!!\n")
        
    else:
        print ("НЕТ\n")
    
