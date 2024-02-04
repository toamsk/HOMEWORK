def month_to_season(m):
  return ['зима', 'весна', 'лето', 'осень'][m % 12 // 3]
x=input('input month: ')
if int(x) > 12:
  print("Число месяцев не может превышать число 12")
else:
  print(month_to_season(int(x)))
