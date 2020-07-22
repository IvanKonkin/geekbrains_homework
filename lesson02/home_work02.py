# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
user_list = input(" >>>  ")


s = list(user_list)

s_even = s[1::2]
s_odd = s[0::2]

min(len(s_odd), len(s_even))
final_list = []
for i in range(min(len(s_odd), len(s_even))):
    final_list.append(s_even[i])
    final_list.append(s_odd[i])
if len(s_odd) > len(s_even):
    final_list.append(s_odd[-1])
if len(s) % 2 == 0:
    print("Список с четным количеством элементов")
else:
    print("Список с нечетным количеством элементов")

print(final_list)






