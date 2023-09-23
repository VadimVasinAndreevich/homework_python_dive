def number_x(number):
    count = 0
    for el in range(1, number + 1):
        if number % el == 0:
            count += 1
    if count == 2:
        print('число является простым')
    else:
        print('число не является простым')


def is_prime(num):
    """
    >>> is_prime(34)
    число является простым
    >>> is_prime(34)
    число не является простым
    >>> is_prime(3.14454)
    Traceback (most recent call last):
    ...
    TypeError: число должно быть целым
    """
    if not isinstance(num, int):
        raise TypeError('число должно быть целым')
    elif num <= 1:
        raise ValueError('число должно быть больше или равно 0')
    elif num >= 100_000:
        raise ValueError('число должно быть меньше или равно 100_000')
    return number_x(num)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
