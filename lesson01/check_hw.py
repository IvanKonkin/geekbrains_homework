a = int(input("Введите количество километров в первый день >>>"))
b = int(input("Введите требуемое количество километров >>>"))

print("1 -й день:", a, "км.")
num_day = 1

while a < b:
    a = a + a * 10 /100
    num_day += 1
    print(num_day,"-й день:", round(a, 2), 'км.')
print("На", num_day, "-й день спортсмен достиг результата - не менее", b, 'км.')