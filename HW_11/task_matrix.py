
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

import random

class Matrix:
    ''' This  class describes only square matrix '''
    default_number = 50
    default_line = 3

    def __init__(self, line=None, number=None, value=None):
        """creaty object class matrix, if max range number not input else default number = 50,
        value matrix may input list of list or generaty random if not input, default line =3"""
        if line is None:
            line = Matrix.default_line
        self.line = line
        if number is None:
            self.__number = Matrix.default_number
        self.__number = number
        if value is None:
            self.value = Matrix.__fill_matrix(self, line, number)
        else:
            self.value = value
    # без else выходит ошибка ... не понятно почему

    def __fill_matrix(self, line, number):
        return [[random.randint(0, number) for _ in range(line)] for _ in range(line)]

    def __str__(self):
        res = "Значение Матрицы\n"
        for item in self.value:
            res += " ".join(map(str, item)) + "\n"
        return res

    def __add__(self, other):
        "This method may summ two object class Matrix"
        result = []
        for item, item2 in zip(self.value, other.value):
            result.append(list(map(sum, zip(item, item2))))
        return Matrix(value=result)

    def __eq__(self, other):
        return self.value is other.value

    def __mul__(self, other):
        result = [[0 for __ in range(len(self.value))] for __ in range(len(self.value))]
        for i in range(len(self.value)):
            for j in range(len(self.value)):
                result[i][j] = sum(self.value[i][k] * other.value[k][j] for k in range(len(self.value)))
        return Matrix(value=result)

    def __repr__(self):
        return f'{Matrix} {self.value}'


if __name__ == "__main__":

    sample = [[1, 2, 3, ],
              [1, 2, 3],
              [1, 2, 3]]
    one = Matrix(3, 10)
    two = Matrix(3, 10)
    # one = Matrix(value=sample)
    # two = Matrix(value=sample)
    print(f'{one=}')
    print(one)
    print(two)
    tree =one + two
    print(tree)
    print(f'проверка на равенство матриц {one == two}')
    # print(one * two)
