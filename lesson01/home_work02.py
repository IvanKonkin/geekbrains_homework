user_answer = int(input("Время в секундах"))
hours = user_answer // 3600
minutes = (user_answer // 60) % 60
seconds = user_answer % 60
if minutes < 10:
    minutes = str('0' + str(minutes))
if seconds < 10:
    seconds = str('0' + str(seconds))
print("{} : {} : {}".format(hours, minutes, seconds))
