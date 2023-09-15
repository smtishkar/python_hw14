# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


import unittest


MAX_VALE =100_000

def num_check(num):
    if num <= 0 or num > MAX_VALE:
        result = "введено не корретное число"
        return result
    elif num > 0 and num < MAX_VALE:
        if num > 2:
            count = 0
            for i in range(1,num):
                if num % i == 0:
                    count += 1 
            if count > 1:
                result = "число составное"
            else:
                result = "число простое"
            return result
        


class TestNumSipmle(unittest.TestCase):
    def test_one_num_simple(self):
        self.assertEqual(num_check(100), 'число составное')

    def test_second_num_simple(self):
        self.assertEqual(num_check(-100), 'введено не корретное число')

    def test_third_num_simple(self):
        self.assertEqual(num_check(7), 'число простое')


if __name__ == '__main__':
    unittest.main(verbosity=2)