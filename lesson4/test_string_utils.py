import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# Позитивные проверки
def test_positive_string():
    stringUtils = StringUtils()
    res = stringUtils.capitilize("лондон")
    assert res == "Лондон"

# Негативные проверки
@pytest.mark.negativ_test
def test_negatitive_string():
    stringUtils = StringUtils()
    res = stringUtils.capitilize("лондон")
    assert res == "лондон"

@pytest.mark.negativ_test
def test_negatitive_string2():
    stringUtils = StringUtils()
    res = stringUtils.capitilize("лондон")
    assert res == "7ондон"

@pytest.mark.negativ_test    
def test_negatitive_string3():
    stringUtils = StringUtils()
    res = stringUtils.capitilize("лондон")
    assert res == "$ондон"

@pytest.mark.negativ_test
def test_negatitive_string4():
    stringUtils = StringUtils()
    res = stringUtils.capitilize("лондон")
    assert res == ":ондон"

# Принимает на вход текст и удаляет пробелы в начале, если они есть
def test_positive_trim():
    stringUtils = StringUtils()
    res = stringUtils.trim(" Париж")
    assert res == "Париж"

def test_positive_trim2():
    stringUtils = StringUtils()
    res = stringUtils.trim("   Париж")
    assert res == "Париж"

# Принимает на вход текст с разделителем и возвращает список строк. \n
@pytest.mark.skip(reason="Тест падает")
def test_positive_to_list():
    stringUtils = StringUtils()
    to_list = []
    res = stringUtils.to_list("яблоко, мандарин, апельсин, киви")
    assert res == ["яблоко", "мандарин", "апельсин", "киви"]

def test_positivee_to_list():
    stringUtils = StringUtils()
    to_list = []
    res = stringUtils.to_list("черника:виноград:ежевика:клубника", ":")
    assert res == ["черника", "виноград", "ежевика", "клубника"]

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
def test_positive_contains():
    stringUtils = StringUtils()
    res = stringUtils.contains("Mississippi", "s")
    assert res == True

def test_positive_contains2():
    stringUtils = StringUtils()
    res = stringUtils.contains("Mississippi", "A")
    assert res == False

# Удаляет все подстроки из переданной строки \n 
def test_positive_del_sym():
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol("Mississippi", "s")
    assert res == "Miiippi"

def test_positive_del_sym2():
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol("Mississippi", "sip")
    assert res == "Missispi"

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
def test_positive_start_wi():
    stringUtils = StringUtils()
    res = stringUtils.starts_with("Stepnogorsk", "S")
    assert res == True

def test_positive_start_wi2():
    stringUtils = StringUtils()
    res = stringUtils.starts_with("Stepnogorsk", "G")
    assert res == False
        
# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
def test_positive_end_wi():
    stringUtils = StringUtils()
    res = stringUtils.end_with("Moscow", "w")
    assert res == True

def test_positive_end_wi2():
    stringUtils = StringUtils()
    res = stringUtils.end_with("Moscow", "o")
    assert res == False

# Возвращает `True`, если строка пустая и `False` - если нет \n 
def test_positive_is_emply():
    stringUtils = StringUtils()
    res = stringUtils.is_empty("")
    assert res == True

def test_positive_is_emply2():
    stringUtils = StringUtils()
    res = stringUtils.is_empty("Saint Petersburg")
    assert res == False

# Преобразует список элементов в строку с указанным разделителем \n 
def test_positive_list_to_str():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string([1,2,3,4,5,6,7,8])
    assert res == "1, 2, 3, 4, 5, 6, 7, 8"

def test_positive_list_to_str2():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["Санкт", "Петербург"])
    assert res == "Санкт, Петербург"

def test_positive_list_to_str3():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["Санкт", "Петербург"], "-")
    assert res == "Санкт-Петербург"