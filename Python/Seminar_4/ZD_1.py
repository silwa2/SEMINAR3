# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!! не округлять константу math.pi

k = 1
num_pi = 0

for i in range (1000000):
    if i % 2 == 0 :
        num_pi += 4 / k
    else :
        num_pi -= 4 / k
    k += 2
print (num_pi)

new_pi = list(str(num_pi))
d = input("Введите d: ")
del new_pi[len(d):]
new_pi=(float(''.join(new_pi)))
print (new_pi)
