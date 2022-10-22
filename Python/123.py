# Напишите программу, которая считывает три числа и подсчитывает сумму чисел.



# massiv = list()

# massiv.append (int(input ("Введите первое число: ")))
# massiv.append (int(input ("Введите второе число: ")))
# massiv.append (int(input ("Введите третье число: ")))
# s=0

# for i in massiv:
#         s += i 
# print (s)


# Напишите программу, которая принимает целое число x 
# и определяет, принадлежит ли данное число промежутку от -1 до 17.

# while True:
#     number = int(input("Введите число: "))

#     for i in range(-1, 18):
#         if number == i:
#             print (f"Число {number} есть в промежутке от -1 до 17")
#             break
#     if number != i:
#         print (f"Числа {number} нет в последовательности от -1 до 17")


# Напишите программу, которая определяет, 
# является ли год с данным номером високосным. 
# Если год является високосным, то выведите «YES», 
# иначе выведите «NO». Год является високосным, 
# если его номер кратен 4, но не кратен 100, или если он кратен 400.

# yars = int(input("Введите год: "))

# if (yars % 4 == 0 and not (yars % 100 ==0)) or (yars % 400 == 0):
#     print ("YES")
# else:
#     print ("NO")


# Даны две различные клетки шахматной доски. 
# Напишите программу, которая определяет, 
# может ли ладья попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, 
# потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом ладьи можно попасть во вторую, 
# или «NO» в противном случае.

# x1 = int(input("Введите число: "))
# y1 = int(input("Введите число: "))
# x2 = int(input("Введите число: "))
# y2 = int(input("Введите число: "))

# if (0<(x1 and x2 and y1 and y2)<8):

#     if (x1 == x2) or (y1==y2):
#         print("YES")
#     else:
#         print ("NO")
# else:
#     print ("Не правильно")


#     1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#         *Пример:*
    
#         - Для N = 5: 1, -3, 9, -27, 81

#     2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#         *Пример:*
    
#         - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#     3. Напишите программу, в которой пользователь будет задавать две строки, а программа - 
#           определять количество вхождений одной строки в другой.

#
# Write a function that takes an integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number. You can guarantee that input is no
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

# ----------------------------------

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# # unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# # unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# # unique_in_order([1,2,2,3,3])       == [1,2,3]

# b = 'AAAABBBCCDAABBB'
# a= list(b)
# c=set(a)

# # print(c)
# text2 = 'AAAABBBCCDAABBB'
# cach = ''
# l = []
# for el in text2:
#     if el != cach:
#         l.append(el)
#         cach = el
# print(l)


# ----------------------------------

# Create a function taking a positive integer as its parameter and returning a string 
# containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the 
# left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 
# 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII;
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# Remember that there can't be more than 3 identical symbols in a row.


# def romanToInt(self, s):
#         result=0
#         f={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#         i=0
#         while i<len(s)-1:
#             if f[s[i+1]]>f[s[i]]:               # Смотрите, если применяются специальные правила
#                 result+=f[s[i+1]]-f[s[i]]
#                 i+=2
#             else:                               # Если не сделано, вывод напрямую
#                 result+=f[s[i]]
#                 i+=1
#         if i<len(s):                            # Второе-последнее специальное правило (используйте i, чтобы судить)
#                 result+=f[s[len(s)-1]]
#         return result


# n= int(input('Введите число: '))
 
# b = ''
# i = 0

# while n > 0:
#     a = n % 2
#     b = str(a) + b
#     n = n // 2
#     if a ==1:
#         i += 1
# print(b,i)



# from collections import OrderedDict as od
# roman = input()
# decimal = 0

# d = (
#         (900, 'CM'),
#         (1000, 'M'),
#         (400, 'CD'),
#         (500, 'D'),
#         (90, 'XC'),
#         (100, 'C'),
#         (40, 'XL'),
#         (50, 'L'),
#         (9, 'IX'),
#         (10, 'X'),
#         (4, 'IV'),
#         (5, 'V'),
#         (1, 'I')
#     )

# d = od(d)

# for k in d:
#     if roman.find(d[k]) >= 0:
#         decimal += k * roman.count(d[k])
#         roman = roman.replace(d[k], '')

# print(decimal)


# text1 = input ('Введите текст:')
# text2 = input ('Введите второй текст:')
# len_find_text = len(text1)
# count = 0
# for i in range (len(text2)):
#     if text2[i: i+len_find_text] == text1:
#         count += 1
# print (count)



# number = int(input('Введите число: '))

# binar_number = bin(number)
# print(binar_number)

# print(binar_number.count('1'))




# line = [1,2,2,3,3]

# list_line = []
# list_line.append(line[0])

# for i in range(len(line)-1):
    
#     if line[i] != line[i+1]:
#         list_line.append(line[i+1])
#     else: continue

# print(list_line)


# def solution(n):
#     roman_numerals = {1000:'M',
#                       900: 'CM',
#                       500: 'D',
#                       400: 'CD',
#                       100: 'C',
#                       90: 'XC',
#                       50: 'L',
#                       40: 'XL',
#                       10: 'X',
#                       9: 'IX',
#                       5: 'V',
#                       4: 'IV',
#                       1: 'I'
#     }
#     roman_string = ''
#     for key in sorted(roman_numerals.keys(),reverse=True):
#         while n >= key:
#             roman_string += roman_numerals[key]
#             n -= key
#     return roman_string

