# Вычислить число c заданной точностью d. Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 -... формула Лейбница

from decimal import*
d = Decimal(input('Введите точность d: '))
a = 1
sum = 0
sign = 1
while 4/a >= d:
    sum += (4/a)*sign
    sign = -sign
    a += 2
print(str(sum)[:len(str(Decimal(d)))])
