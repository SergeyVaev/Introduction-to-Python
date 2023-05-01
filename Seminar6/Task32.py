# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


# создадим рандомный список и выведем его в одну строку.
import random

my_lists = []

for i in range(10):
    my_lists.append(random.randint(1, 100))

print(' '.join(map(str, my_lists)))

min_num = int(input('Введите минимальное число из диапазона: '))
max_num = int(input('Введите максимальное число из диапазона: '))

for i in range(len(my_lists)):
    if min_num <= my_lists[i] <= max_num:
        print(i)


    
    