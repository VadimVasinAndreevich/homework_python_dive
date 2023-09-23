import unittest


def number_x(number):
    count = 0
    for el in range(1, number + 1):
        if number % el == 0:
            count += 1
    if count == 2:
        return 'число является простым'
    else:
        return 'число не является простым'


class TestCaseName(unittest.TestCase):
    def test_param(self):
        self.assertEqual(type(num), int, msg='это не целое число')

    def test_number_up(self):
        self.assertLessEqual(num, 100_000, msg='число не может быть больше 100 тыс.')

    def test_number_down(self):
        self.assertGreaterEqual(num, 1, msg='число не может быть меньше 1')

    def test_operation(self):
        self.assertEqual(type(res), str, msg='это не строка')

    def test_result(self):
        self.assertEqual(res, 'число является простым', msg='значит число сложное')


num = 45
res = number_x(num)


if __name__ == '__main__':
    unittest.main()
