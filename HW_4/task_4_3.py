# ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». ✔Напишите функцию, которая при
# запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s)
# на None. ✔Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = "Ivan"
s = 12
boxs = 12
goods = "meat"

def change_globals():
    new =dict()
    result = globals()
    for k, i in result.items():    
              if k[-1:] == "s" and len(k) > 1:
                result[k] = None
                new[k[0:-1]] = i
    for k, i in new.items():
         result[k] = i
    return     
   
change_globals()    
print(globals())
      



