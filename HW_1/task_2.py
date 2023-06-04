# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.


def check_triangle(side1, side2, side3):

    if (side2 + side3) < side1 or (side1 + side2) < side3 or (side1+side3) < side2:
        print('такого треугольника не существует')
    else:
        if side1 == side2 == side3:
             print('треугольник равносторонний')
        else:
            print('треугольник разносторонний')
            if (side1 == side2 and side3 != side1) or (side2 == side3 and side1 != side2) \
                    or (side3 == side1 and side2 != side3):
                print('треугольник равнобедренный')



check_triangle(9,6,6)
