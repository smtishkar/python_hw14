# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

import pytest


year = 2000
year2 = 2001
year3 = 'RIDK'
MAIN_LEAP_CRYTERIA = 4
ADDITIONAL_LEAP_CRYTERIA = 400
LEAP_EXCLUDINGG_CRYTERIA = 100

def year_type(year):
    try:
        year == int(year)
        if year % MAIN_LEAP_CRYTERIA == 0 and year%LEAP_EXCLUDINGG_CRYTERIA !=0 or year %ADDITIONAL_LEAP_CRYTERIA == 0:
            result = "Год высокосный"
        else: 
            result = "Год обычный"
        return result
    except:
        result = "введено не корректное значение"
        return result

def test_one_year_type():
    assert year_type(year) == 'Год высокосный'

def test_two_year_type():
    assert year_type(year2) == 'Год обычный'

def test_three_year_type():
    assert year_type(year3) == 'введено не корректное значение'

if __name__ == '__main__':
    pytest.main()