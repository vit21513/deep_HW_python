class Triangle_Exception(BaseException):
    def __str__(self):
        return f"Triangle exception"


class Exception_side_none(Triangle_Exception):

    def __str__(self):
        return f"Triangle side not can is NONE"


class Exception_Triangle_incorrect(Triangle_Exception):

    def __str__(self):
        return f'Tакого треугольника не существует'


def check_triangle(side1=None, side2=None, side3=None):
    if side1 is None or side2 is None or side3 is None:
        raise Exception_side_none()
    try:
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise Exception_Triangle_incorrect()
        if (side2 + side3) < side1 or (side1 + side2) < side3 or (side1 + side3) < side2:
            raise Exception_Triangle_incorrect()
    except TypeError as e:
        print(e)
    else:
        try:
            if side1 == side2 == side3:
                print('треугольник равносторонний')
            else:
                print('треугольник разносторонний')
        except Triangle_Exception():
            print("Что-то пошло не так")


if __name__ == "__main__":
    check_triangle(10, 10, 9)
    check_triangle()
