my_dict = {
            'один': 1,
            'два': 2,
            'три': 3,
            'четыре': 4,
            'пять': 5
        }


class Int:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if other in my_dict:
            return self.value + my_dict[other]
        elif isinstance(other, str) and other not in str(my_dict):
            return "TypeError: справа от знака " + " непонятный текст. Если что, я понимаю текстом цифры с 1 по 5."
        elif isinstance(other, tuple):
            return "TypeError: unsupported operand type(s) for +: 'Int' and 'tuple."
        return self.value + int(other)


def decor(func):
    def wrapper(a, b):
        if b in my_dict:
            return func(a, my_dict[b])
        elif isinstance(b, str) and b not in str(my_dict):
            return "TypeError: справа от знака " + " непонятный текст. Если что, я понимаю текстом цифры с 1 по 5."
        elif isinstance(b, tuple):
            return "TypeError: unsupported operand type(s) for +: 'Int' and 'tuple."
        return func(a, int(b))
    return wrapper


@decor
def my_sum(a, b):
    return a + b


# использование
x = Int(5)
print(x + '5')  # 10
print(x + 'один')  # 6
print(x + 'пять')  # 10
print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'

print()

x = 5
print(my_sum(x, '5'))  # 10)
print(my_sum(x, 'один'))  # 6)
print(my_sum(x, 'пять'))  # 10
print(my_sum(x, 'шесть'))  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
print(my_sum(x, 'a'))  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
print(my_sum(x, (1,)))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
