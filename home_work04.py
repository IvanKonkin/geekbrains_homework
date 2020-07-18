# user_number = int(input("Введите целое положительное число"))
# array = str(user_number)
# print(max(array))

user_number = int(input("Введите целое положительное число"))
last_number = user_number % 10

while user_number > 0:
    if user_number % 10 > last_number:
        last_number = user_number % 10
    user_number = user_number // 10
print(last_number)
