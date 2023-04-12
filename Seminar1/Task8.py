# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_length = int(input('Введите длинну шоколадки: '))
chocolate_width = int(input('Введите ширину шоколадки: '))
k = int(input('введите колличество долек которые хотите отломить: '))
if k < chocolate_length * chocolate_width:
    if k % chocolate_length == 0 or k % chocolate_width == 0:
        print('yes')
    else:
        print('no')
else:
    print('XD')
