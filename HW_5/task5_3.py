# Создайте функцию генератор чисел Фибоначчи



def fibonachi(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    yield a

print(*fibonachi(2))    
print(*fibonachi(20))    