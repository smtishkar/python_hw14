# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

import unittest

matrix = [[1,2,3],[4,5,6]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]


def matrix_transposition(matrix : list) -> list:
    new_matrix =  [ [0]* len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            new_matrix[j][i]= matrix [i][j]
    return new_matrix

def print_matrix (matrix: list):
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            print (matrix[i][j], end=' ')
        print()



class Testmatrix_transposition(unittest.TestCase):
    def test_one_matrix_transposition(self):
        self.assertEqual(matrix_transposition(matrix), [[1, 4], [2, 5], [3, 6]])

    def test_two_matrix_transposition(self):
        self.assertEqual(matrix_transposition(matrix2), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])


if __name__ == '__main__':
    unittest.main(verbosity=2)