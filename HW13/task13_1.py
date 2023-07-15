
class incorect_input(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'incorect input value, value {self.name} must >1 and < 1000'



def check_quanty_digits(num):
    if 1 <= num <= 999:
        res_len = 0
        while num > 1:
            num = num / 10
            res_len += 1
        return res_len
    raise incorect_input(num)


print(check_quanty_digits(111))
