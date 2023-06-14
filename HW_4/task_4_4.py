# ✔Напишите функцию для транспонирования матрицы

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,8,7,6],
          [5,4,5,2]]

def transpon_matrix(list_matrix):
     new_matrix = zip(*list_matrix)
    #  так как он вернет кортеж я не стал его переводить в список
     return new_matrix


print(*transpon_matrix(matrix))

