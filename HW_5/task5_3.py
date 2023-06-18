# Создайте функцию генератор чисел Фибоначчи



def fibonachi(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    yield a

print(*fibonachi(2))    
print(*fibonachi(20))    