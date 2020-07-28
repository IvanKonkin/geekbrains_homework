def exe_5():
    res = 0
    while True:
        numbers = input('Введите список чисел через пробел или * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма чисел =  {res}. Программа завершена')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или *')
        print(f'Сумма чисел = {res}')

exe_5()