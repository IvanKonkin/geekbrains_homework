income = float(input("Укажите вашу выручку за период"))
costs = float(input("Укажите сумму издержек за период"))
profit = income - costs
losses = costs - income
profitability = profit / income
if income > costs:
    print(f"Вы отработали период с прибылью в размере - + {profit}")
    print(f"Рентабильность =  {profitability}")
if costs > income:
    print(f"Вы отработали период в минус. Сумма издержек -  + {losses}")

employees = int(input("Сколько сотрудников у вас в штате ?"))
per_employee = profit / employees
print(f"Прибыль на сотруднка  = {per_employee}")

