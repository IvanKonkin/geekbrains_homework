username = input("Как вас зовут ?")
weight = int(input("Сколько вы весите"))
height = int(input("Какой у вас рост?")) / 100
fat_index = weight / (height ** 2)

if fat_index <= 16:
    print(f"Привет {username}! У тебя недобор по весу")
if 18 <= fat_index < 25:
    print(f"Привет {username}! Твой вес в норме")
elif fat_index >= 25:
    print(f"Привет {username}! У тебя излишний вес")
