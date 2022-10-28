class Int:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        my_dict = {
            'один': 1,
            'два': 2,
            'три': 3,
            'четыре': 4,
            'пять': 5
        }

        if other in my_dict:
            return self.value + my_dict[other]
        elif isinstance(other, str) and other not in str(my_dict):
            return "TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5."
        elif isinstance(other, tuple):
            return "TypeError: unsupported operand type(s) for +: 'Int' and 'tuple."
        return self.value + int(other)


# использование
x = Int(5)
print(x + '5')  # 10
print(x + 'один')  # 6
print(x + 'пять')  # 10
print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'


