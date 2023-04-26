# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
def sum(first_number,second_number):
    if second_number == 0:
        return first_number
    return sum(first_number+1,second_number-1)
print (result := (sum(first_number,second_number)))
        

   