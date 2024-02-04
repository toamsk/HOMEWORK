is_year_leap = input ("Введите год: ")
if (int(is_year_leap) % 4):
    print (("Год " + (is_year_leap) + " не високосный"))
else: 
    print (("Год " + (is_year_leap) + " високосный"))