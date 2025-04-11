#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и
# возвращающую 3 значения (с помощью кортежа, после return перечислить
# все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.


def square(one_size):
    perimeter = one_size * 4
    area = one_size ** 2
    diagonal = one_size * (2 ** 0.5)
    return perimeter, area, diagonal


print (square (5))