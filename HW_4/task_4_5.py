# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


from attr import has


def dict_return(*,x):
    temp = x
    result = {}
    if x is temp:
        result[str(x)] = "x"
    else:
        result[hash(x)] = "x"
    return result    

print(dict_return(x=[99,12,"2"]))
print(dict_return(x=12))
