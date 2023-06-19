# Создайте функцию генератор чисел Фибоначчи


def fibonachi(n):

    a,b = 0,1
    res = [0]
    for _ in range(n):
        a, b = b, a + b
        res.append(a)
    yield res


print(*fibonachi(2))
print(*fibonachi(20))
