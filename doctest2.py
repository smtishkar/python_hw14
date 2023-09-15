# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]



my_list = [1, 2, 3, 1, 2, 4, 5]
my_list2 = [1, 2, 3, 7, 7, 1, 2, 4, 5]
my_list3 = []

def unique_el (my_list):
    """
    >>> unique_el(my_list)
    [1, 2]
    >>> unique_el(my_list2)
    [1, 2, 7]
    >>> unique_el(my_list3)
    []
    """
    new_list = []
    for elem in my_list:
        if my_list.count(elem) > 1:
            new_list.append(elem)
    print(list(set(new_list)))



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    unique_el(my_list)
    unique_el(my_list2)
    unique_el(my_list3)