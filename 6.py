# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
#
# Пример
#
# -Для "abababb" и "aba" -> 2
#***********
str1 = (input())
str2 = (input())
count = 0
for i in range(0, len(str1)+1):
    if str2 in str1[i:len(str2)+i]:
        count = count + 1
print(str1, str2, "->", count)
