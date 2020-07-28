def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print(my_func((int(input('Введите делимое число: '))), (int(input('Введите делитель: ')))))
