"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

side_tringle_a = int(input('Введите величину стороны "a" треугольника: '))
side_tringle_b = int(input('Введите величину стороны "b" треугольника: '))
side_tringle_c = int(input('Введите величину стороны "c" треугольника: '))
if side_tringle_a + side_tringle_b > side_tringle_c and \
    side_tringle_a + side_tringle_c > side_tringle_b and \
    side_tringle_b + side_tringle_c > side_tringle_a:
    print(f'Треугольник со сторонами {side_tringle_a}, {side_tringle_b}, {side_tringle_c} '
          f'существует')
    if side_tringle_a == side_tringle_b == side_tringle_c:
        print('треугольник равносторонний')
    elif side_tringle_a == side_tringle_b or side_tringle_a == side_tringle_c or \
        side_tringle_b == side_tringle_c:
        print('треугольник равнобедренный')
else:
    print(f'Треугольник со сторонами {side_tringle_a}, {side_tringle_b}, {side_tringle_c} '
          f'не существует')
