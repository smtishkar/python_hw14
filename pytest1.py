# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

import pytest

name = ['Вадим', 'Сергей', 'Андрей']
salary = [100_000, 150_000, 130_000]
bonus = ['10.25%', '5.55%', '6.89%']

name2 = ['Вадим', 'Сергей']
salary2 = [100_000, 150_000, 130_000]
bonus2 = ['10.25%', '5.55%', '6.89%']


def common_dict_creation(name: dict, salary: dict, bonus: dict):
    result_dict = {name: (
        salary * float(bonus[:-1]))/100 for name, salary, bonus in zip(name, salary, bonus)}
    return result_dict

print(common_dict_creation(name,salary,bonus))


def test_one_common_dict_creation():
    assert common_dict_creation(name,salary,bonus) == {'Вадим': 10250.0, 'Сергей': 8325.0, 'Андрей': 8957.0}


def test_two_common_dict_creation():
    assert common_dict_creation(name2,salary2,bonus2) == {'Вадим': 10250.0, 'Сергей': 8325.0}


if __name__ == '__main__':
    pytest.main()