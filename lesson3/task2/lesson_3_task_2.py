
from smartphone import Smartphone

catalog = [
    Smartphone("sumsung,", "A5,", "+79254572565"),
    Smartphone("iPhone,", "12,", "+79254572565"),
    Smartphone("Xiaomi,", "12,", "+79254572565"),
    Smartphone("OnePlus,", "8 Pro,", "+79404445566"),
    Smartphone("Xiaomi,", "Mi 11,", "+79505556677")
]

for i in catalog:
    print(i.brand, i.model, i.number)    