# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from shutil import register_unpack_format


def is_statement(x, y, z):
    a = not(x or y or z)
    b = not x and not y and not z
    return(a==b)
xyz = list(map(bool,input('Введите значения x y z через пробел: ').split()))
print(is_statement(xyz[0], xyz[1], xyz[2]))