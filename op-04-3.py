# Пользователь делает вклад в размере a рублей сроком на years лет
# под 10% годовых (каждый год размер его вклада увеличивается на 10%.


def bank(money,years):
  for a in range(1, years+1):
    profit = money * 0.1
    money = profit + money
    print(f"Год {a}, сумма на счету {money}")
  return money


bank(100, 4)