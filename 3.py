# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
#
# Пример:
#
# Для n = 6 -> 14.072
#***********
n = int(input())
coll = []
result = 1
for i in range(1, n+1):
    result = (1+1/i)**i
    coll.append(result)
sum = 0
for i in range(0, n):
    sum += coll[i]
print(round(sum, 3))
