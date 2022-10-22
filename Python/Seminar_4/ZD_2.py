# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


number=input("Введите натуральное число N: ")

try:
    number1 = int(number)
    for i in range(1, number1+1):
        if(number1%i==0):
            print(i)
except ValueError:
    print("Это не правильный ввод, попробуйте еще раз.")
   
