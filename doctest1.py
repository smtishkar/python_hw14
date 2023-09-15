# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.



def check_triangle(a: int,b: int,c: int):
    """
    >>> check_triangle(4,4,4)
    Треугольник равносторонний
    >>> check_triangle(4,5,3)     
    Треугольник разносторонний
    >>> check_triangle(4,5,4)     
    Треугольник равнобедренный

    """

    check_1 = a + b
    check_2 = a + c
    check_3 = c + b

    if check_1 < c or check_2 < b or check_3 < a:
        print("треугольник не существует")
    else:
        if a == b and b == c:
            print("Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный")
        else: 
            print("Треугольник разносторонний")



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)