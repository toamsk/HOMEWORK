from mailing import Mailing
from address import Address

#создание адресов
to_address = Address("021500", "г. Степногорск,", "ул. Серова,", "дом 8", "кв. 5")
from_address = Address("021501", "г. Москва,", "ул. Винницкая,", "дом 5", "кв. 175")

# Создание почтового отправления
mailing = Mailing(to_address, from_address, 500, "RU1234567890")


print("Отправление", mailing.track, "из", mailing.from_address.index, mailing.from_address.city, mailing.from_address.street, mailing.from_address.house,"-", mailing.from_address.flat, "в", mailing.to_address.index, mailing.to_address.city, mailing.to_address.street, mailing.to_address.house, "-", mailing.to_address.flat, ".", "Стоимость отправления", mailing.cost, "рублей")
