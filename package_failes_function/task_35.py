"""
Создайте функцию генератор чисел Фибоначчи
"""


def fib(x=0, y=1):
    for el in range(0, 100):
        el = x + y
        x, y = y, el
        yield el


res = fib()
print(*res)
