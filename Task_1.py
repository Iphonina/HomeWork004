# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

import sympy


def polynomial():
    k = int(input('Введите максимальную степень числа: '))
    my_dict = {}
    for i in range(k, -1, -1):
        y = random.randint(0, 100)
        my_dict[i] = y
    print(my_dict)
    poly = ''
    for n in range(k, -1, -1):
        if my_dict[n] == 0:
            poly += f''
        elif n == 0:
            poly += f'{my_dict[n]}'
        elif n == 1:
            poly += f'{my_dict[n]}*x + '
        else:
            poly += f'{my_dict[n]}*x**{n} + '
    poly += ' = 0'
    return poly


poly_1 = polynomial()
print(poly_1)
with open('file.txt', 'w') as data:
    data.write(f'{poly_1}')
poly_2 = polynomial()
print(poly_2)
with open('file_2.txt', 'w') as data:
    data.write(f'{poly_2}')
