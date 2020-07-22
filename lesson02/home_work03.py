# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


user_month = int(input("Введите номер месяца в виде целого числа от 1 до 12  >>>  "))

while user_month > 12 or user_month <= 0:
    user_month = int(input("Введите номер месяца в виде целого числа от 1 до 12  >>>  "))


season_dict = dict(winter=[1, 2, 12], spring=[3, 4, 5], summer=[6, 7, 8], autumn=[9, 10, 11])

for key in season_dict:
    if user_month in season_dict[key]:
        print(key)
