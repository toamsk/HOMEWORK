import pytest
from string_utils import StringUtils

string_Utils = StringUtils()

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст

@pytest.mark.parametrize( 'text1, result', [("лондон", "Лондон"), ("лондон", "лондон"), ("лондон", "7ондон"), ("лондон", "$ондон"), ("лондон", ":ондон")] )
def test_positive_string(text1, result):
    string_Utils = StringUtils()
    res = string_Utils.capitilize(text1)
    assert res == result

# Принимает на вход текст и удаляет пробелы в начале, если они есть

@pytest.mark.parametrize( 'text2, result2', [(" Париж", "Париж"), ("  Париж", "Париж"), ("Париж", "Париж"), (" ", "")] )
def test_positive_trim2(text2, result2):
    string_Utils = StringUtils()
    res = string_Utils.trim(text2)
    assert res == result2

# Принимает на вход текст с разделителем и возвращает список строк. \n
#@pytest.mark.skip(reason="Тест падает, найден баг")
@pytest.mark.xfail
def test_positive_to_list():
    string_Utils = StringUtils()
    to_list = []
    res = string_Utils.to_list("яблоко, мандарин, апельсин, киви")
    assert res == ["яблоко", "мандарин", "апельсин", "киви"]

def test_positivee_to_list():
    string_Utils = StringUtils()
    to_list = []
    res = string_Utils.to_list("черника:виноград:ежевика:клубника", ":")
    assert res == ["черника", "виноград", "ежевика", "клубника"]

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
def test_positive_contains():
    string_Utils = StringUtils()
    res = string_Utils.contains("Mississippi", "s")
    assert res is True

def test_positive_contains2():
    string_Utils = StringUtils()
    res = string_Utils.contains("Mississippi", "A")
    assert res is False

def test_positive_contains2():
    string_Utils = StringUtils()
    res = string_Utils.contains("Mississippi", " ")
    assert res is False
  
# Удаляет все подстроки из переданной строки \n 
@pytest.mark.parametrize( 'text3, text4, result3', [("Mississippi", "s", "Miiippi"), ("Mississippi", "sip", "Missispi") ] )
def test_positive_delete_symbol(text3, text4, result3):
    string_Utils = StringUtils()
    res = string_Utils.delete_symbol(text3, text4)
    assert res == result3

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
def test_positive_start_wi():
    string_Utils = StringUtils()
    res = string_Utils.starts_with("Stepnogorsk", "S")
    assert res is True

def test_positive_start_wi2():
    string_Utils = StringUtils()
    res = string_Utils.starts_with("Stepnogorsk", "G")
    assert res is False
        
# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
def test_positive_end_wi():
    string_Utils = StringUtils()
    res = string_Utils.end_with("Moscow", "w")
    assert res is True

def test_positive_end_wi2():
    string_Utils = StringUtils()
    res = string_Utils.end_with("Moscow", "o")
    assert res is False

# Возвращает `True`, если строка пустая и `False` - если нет \n 
def test_positive_is_emply():
    string_Utils = StringUtils()
    res = string_Utils.is_empty("")
    assert res is True

def test_positive_is_emply2():
    string_Utils = StringUtils()
    res = string_Utils.is_empty("Saint Petersburg")
    assert res is False

# Преобразует список элементов в строку с указанным разделителем \n 
def test_positive_list_to_str():
    string_Utils = StringUtils()
    res = string_Utils.list_to_string([1,2,3,4,5,6,7,8])
    assert res == "1, 2, 3, 4, 5, 6, 7, 8"

def test_positive_list_to_str2():
    string_Utils = StringUtils()
    res = string_Utils.list_to_string(["Санкт", "Петербург"])
    assert res == "Санкт, Петербург"

def test_positive_list_to_str3():
    string_Utils = StringUtils()
    res = string_Utils.list_to_string(["Санкт", "Петербург"], "-")
    assert res == "Санкт-Петербург"