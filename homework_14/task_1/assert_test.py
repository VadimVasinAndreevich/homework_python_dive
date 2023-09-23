import pytest


def number_x(number):
    count = 0
    for el in range(1, number + 1):
        if number % el == 0:
            count += 1
    if count == 2:
        return 'число является простым'
    else:
        return 'число не является простым'


def test_num():
    assert type(num) == int, 'Математика покинула чат'


def test_number_up():
    assert num <= 100_000, 'число не может быть больше 100 тыс.'


def test_number_down():
    assert num >= 1, 'число не может быть меньше 1'


def test_res():
    assert type(res) == str, 'кто же это не знает'


def test_print_res():
    assert res == 'число является простым', 'может и не такое простое как кажется)'


num = 37
res = number_x(num)


if __name__ == '__main__':
    pytest.main()
