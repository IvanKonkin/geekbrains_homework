# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


s = [7, 6, 5, 4, 3, 2]

tryCount = 5
#
i = 0
while i < tryCount:
    user = int(input("Введите число >>> "))
    s.append(user)
    s.sort(reverse=True)
    print(s)
    i = i + 1



