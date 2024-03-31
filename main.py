import math
from tabulate import tabulate


def func(x):
    # return x**2
    return 4 * x ** 3 - 5 * x ** 2 + 6 * x - 7
    # return 1/math.log(x)
    # return math.cos(x)/(x+2)
    # return math.sqrt(1 + 2 * x ** 2 - x ** 3)
    # return 1/math.sqrt(3+x**5)
    # return math.sqrt(x**2+3)
    # return math.sqrt(x**3+4)
    # return x**2 - 3*x


def get_parameters():
    a = float(input('Введите начало отрезка: '))
    b = float(input('Введите конец отрезка: '))
    return a, b


def get_method():
    n = 8
    print('\t', '1: Метод прямоугольников')
    print('\t', '2. Метод трапеций')
    print('\t', '3. Метод Симпсона')
    param = int(input('Введите номер метода, котрый хотите использовать: '))
    if param == 1:
        a, b = get_parameters()
        rectangle_method(n, a, b)
    elif param == 2:
        a, b = get_parameters()
        trapezoid_method(n, a, b)
    elif param == 3:
        a, b = get_parameters()
        simpson_method(n, a, b)


def rectangle_method(n, a, b):
    h = (b - a) / n
    x_array = []
    print('Разменр шага: ' + str(h))
    i = a
    while i < b:
        i += h
        x_array.append(i)
    if len(x_array) > n:
        del x_array[n]
    print(x_array)
    y_right_array = []
    for x in x_array:
        y_right_array.append(func(x))
    print(y_right_array)
    I_right = h * sum(y_right_array)
    print('Значение интеграла для правых прямоугольников: ' + str(I_right))
    y_left_array = []
    for x in x_array:
        x -= h
        # print(x)
        y_left_array.append(func(x))
    print(y_left_array)
    I_left = h * sum(y_left_array)
    print('Значение интеграла для левых прямоугольников: ' + str(I_left))
    y_middle_array = []
    for x in x_array:
        x -= h / 2
        print(x)
        y_middle_array.append(func(x))
    print(y_middle_array)
    I_middle = h * sum(y_middle_array)
    print('Значение интеграла для средних прямоугольников: ' + str(I_middle))


def trapezoid_method(n, a, b):
    h = (b - a) / n
    print('Величина шага: '+str(h))
    x_array = []
    i = a
    table = []
    headers = []
    iterator = 0
    x_array.append(i)
    while i < b:
        headers.append(str(iterator))
        i += h
        x_array.append(i)
        iterator += 1
    headers.append(str(iterator))
    if len(x_array) > n + 1:
        del x_array[n + 1]
    table.append(x_array)
    y_array = []
    for x in x_array:
        y_array.append(func(x))
    table.append(y_array)
    print(tabulate(table, headers=headers, tablefmt="pretty"))
    incomplete_array = y_array[1:-1]
    I_trap = h * ((y_array[0] + y_array[n]) / 2 + sum(incomplete_array))
    print('Значение интеграла: ' + str(I_trap))


def simpson_method(n, a, b):
    if n % 2 != 0:
        print("Значение n для этого метода должно быть чётным иначе результат вычисления будет некорректным")
        return
    h = (b - a) / n
    print('Величина шага: '+ str(h))
    x_array = []
    i = a
    table = []
    headers = []
    iterator = 0
    x_array.append(i)
    while i < b:
        headers.append(str(iterator))
        i += h
        x_array.append(i)
        iterator += 1
    headers.append(iterator)
    if len(x_array) > n + 1:
        del x_array[n + 1]
    table.append(x_array)
    y_array = []
    for x in x_array:
        y_array.append(func(x))
    table.append(y_array)
    incomplete_array = y_array[1:-1]
    even_numbers_array = []
    odd_number_array = []
    for i in range(len(incomplete_array)):
        if i % 2 == 0:
            even_numbers_array.append(incomplete_array[i])
        else:
            odd_number_array.append(incomplete_array[i])
    print(tabulate(table, headers=headers, tablefmt="pretty"))
    I = h / 3 * (y_array[0] + 4 * sum(even_numbers_array) + 2 * sum(odd_number_array) + y_array[n])
    print('Значение интеграла: '+str(I))


get_method()
