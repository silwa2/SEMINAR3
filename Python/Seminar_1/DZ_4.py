# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


while True:
    
    quarter = int(input ("Введите номер четверти: "))
    
    if quarter == 1:
        print("x > 0 and y > 0")
        
    elif quarter == 2:
        print("x < 0 and y > 0")
        
    elif quarter == 3:
        print("x < 0 and y < 0")
        
    elif quarter == 4:
        print("x > 0 and y < 0")
        
    else:
        print("Номер четветри может принимать значение от 1 до 4.\n")
        