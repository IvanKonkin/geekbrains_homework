# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user_answer = input("Введите несколько слов, разделённых пробелами")

separate_str = user_answer.split()
for index, value in enumerate(separate_str, 1):
    print("{}. {}".format(index, value))




