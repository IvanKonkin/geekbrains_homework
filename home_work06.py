first_day = int(input("Введите результат первого дня "))
result = int(input("Введите желаемый результат "))
day_number = 0


while first_day < result:
    first_day *= 1.1
    day_number += 1

print(f"Вы достигнете желаемого результата на {day_number} день")