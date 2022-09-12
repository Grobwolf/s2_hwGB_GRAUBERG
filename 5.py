# Задание 5 Реализуйте алгоритм перемешивания списка.
#***********
import random

coll = []
N = int(input())
for i in range(1, N+1):
    coll.append(random.randrange(999))
print(coll)
shuffled_coll = coll.copy()
for i in range(0, N):
    random_index = random.randrange(0, N)
    shuffled_coll[i], shuffled_coll[random_index] = shuffled_coll[random_index], shuffled_coll[i]
print(shuffled_coll)
#Или вариант через метод shuffle
coll = []
N = int(input())
for i in range(1, N+1):
    coll.append(random.randrange(999))
print(coll)
random.shuffle(coll)
print(coll)