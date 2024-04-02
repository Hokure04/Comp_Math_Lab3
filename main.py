import math
from sympy import integrate, Symbol
from tabulate import tabulate


def choose_function():
    print('1. x**2')
    print('2. 4*x**3 - 5*x**2 + 6*x - 7')
    print('3. 1/ (x**2 - 3*x)')
    func_number = int(input('Введите номер функции: '))
    return func_number


def func(number, x):
    if number == 1:
        return x ** 2
    elif number == 2:
        return 4 * x ** 3 - 5 * x ** 2 + 6 * x - 7
    elif number == 3:
        return 1 / (x**2 - 3*x)


def get_parameters():
    a = float(input('Введите начало отрезка: '))
    b = float(input('Введите конец отрезка: '))
    if a > b:
        print('Сначала должно быть введено значение расположенное левее, попробуйте ещё раз')
        while a > b:
            a = float(input("Введите точку a: "))
            b = float(input("Введите точку b: "))
    e = float(input("Введите точночть: "))
    if e < 0:
        while e < 0:
            print('Точность не может быть меньше нуля, попробуйте ещё раз')
            e = float(input("Введите точночть: "))
    return a, b, e


def check_divergence(value):
    if math.isinf(value) or math.isnan(value):
        print("Данный интеграл расходится.")
        return -1


def get_method():
    while True:
        n = 4
        print('\t', '1: Метод прямоугольников')
        print('\t', '2. Метод трапеций')
        print('\t', '3. Метод Симпсона')
        try:
            param = int(input('Введите номер метода, котрый хотите использовать: '))
            if param == 1:
                number = choose_function()
                a, b, e = get_parameters()
                rectangle_method(number, n, a, b, e)
            elif param == 2:
                number = choose_function()
                a, b, e = get_parameters()
                trapezoid_method(number, n, a, b, e)
            elif param == 3:
                number = choose_function()
                a, b, e = get_parameters()
                simpson_method(number, n, a, b, e)
        except TypeError:
            print('К сожалению данный интеграл расходится')


def rectangle_method(number, n, a, b, e):
    x = Symbol("x")
    I_true = integrate(func(number, x), (x, a, b))
    # print(I_true)
    I_middle = 0
    iter = 0
    while abs(I_true - I_middle) > e:
        if iter > 0:
            n *= 2
        h = (b - a) / n
        table, headers, x_array = [], [], []
        print('Разменр шага: ' + str(h))
        i = a
        iterator = 0
        while i < b:
            headers.append(str(iterator))
            iterator += 1
            i += h
            x_array.append(i)
        if len(x_array) > n:
            del x_array[n]
        headers.append(str(iterator))
        table.append(x_array)
        y_right_array = []
        for x in x_array:
            y_right_array.append(func(number, x))
        table.append(y_right_array)
        I_right = h * sum(y_right_array)
        if check_divergence(I_right) == -1:
            break
        print('Значение интеграла для правых прямоугольников: ' + str(I_right))
        y_left_array = []
        for x in x_array:
            x -= h
            # print(x)
            y_left_array.append(func(number, x))
        table.append(y_left_array)
        I_left = h * sum(y_left_array)
        if check_divergence(I_left) == -1:
            break
        print('Значение интеграла для левых прямоугольников: ' + str(I_left))
        y_middle_array = []
        for x in x_array:
            x -= h / 2
            y_middle_array.append(func(number, x))
        I_middle = h * sum(y_middle_array)
        if check_divergence(I_middle) == -1:
            break
        print('Значение интеграла для средних прямоугольников: ' + str(I_middle))
        table.append(y_middle_array)
        print(tabulate(table, headers=headers, tablefmt="pretty"))
        iter += 1


def trapezoid_method(number, n, a, b, e):
    x = Symbol("x")
    I_true = integrate(func(number, x), (x, a, b))
    print(I_true)
    I_trap = 0
    iter = 0
    while abs(I_true - I_trap) > e:
        if iter > 0:
            n *= 2
        h = (b - a) / n
        print('Величина шага: ' + str(h))
        x_array, table, headers = [], [], []
        i = a
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
            y_array.append(func(number, x))
        table.append(y_array)
        print(tabulate(table, headers=headers, tablefmt="pretty"))
        incomplete_array = y_array[1:-1]
        I_trap = h * ((y_array[0] + y_array[n]) / 2 + sum(incomplete_array))
        if check_divergence(I_trap) == -1:
            break
        print('Значение интеграла: ' + str(I_trap))
        iter += 1


def simpson_method(number, n, a, b, e):
    if n % 2 != 0:
        print("Значение n для этого метода должно быть чётным иначе результат вычисления будет некорректным")
        return
    x = Symbol("x")
    I_true = integrate(func(number, x), (x, a, b))
    I_simps = 0
    iter = 0
    while abs(I_true - I_simps) > e:
        if iter > 0:
            n *= 2
        h = (b - a) / n
        print('Величина шага: ' + str(h))
        x_array, table, headers = [], [], []
        i = a
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
            y_array.append(func(number, x))
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
        I_simps = h / 3 * (y_array[0] + 4 * sum(even_numbers_array) + 2 * sum(odd_number_array) + y_array[n])
        if check_divergence(I_simps) == -1:
            break
        print('Значение интеграла: ' + str(I_simps))
        iter += 1


get_method()
