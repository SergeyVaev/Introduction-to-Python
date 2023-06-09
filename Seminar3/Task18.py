# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
# Запрашиваем у пользователя количество элементов в массиве
n = int(input('Укажите колличество эллементов: ')) 
# Запрашиваем у пользователя сам массив чисел, преобразуя строку в список целых чисел
a = [random.randint(0, 10) for i in range(n)] 
print(a)
# Запрашиваем у пользователя число X
x = int(input('Укажите число x : ')) 
# Инициализируем переменную минимальной разницы значением разницы между X и первым элементом массива
mindiff = abs(x - a[0]) 
# Инициализируем переменную минимального элемента значением первого элемента массива
minelem = a[0] 
# Проходим по всем элементам массива, начиная со второго
for i in range(1, n): 
    # Вычисляем разницу между X и текущим элементом
    diff = abs(x - a[i]) 
    # Если разница меньше минимальной разницы
    if diff < mindiff: 
        # Обновляем значение минимальной разницы
        mindiff = diff 
        # Обновляем значение минимального элемента
        minelem = a[i] 
# Выводим найденный минимальный элемент
print(minelem)
