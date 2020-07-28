def result(**user_info):
    return list(user_info.values())


def arguments():
    print(result(name=input('Имя : '),
                s_name=input('Фамилия : '),
                b_date=input('Дата рождения : '),
                l_town=input('Город проживания : '),
                email=input('Электронная почта : '),
                tel=input('Номер телефона : ')))


arguments()
