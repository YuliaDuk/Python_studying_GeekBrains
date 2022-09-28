# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите количество чисел (n) последовательности (1+1/n)^n: '))
if n<=0:
    print('Число n не может быть меньше или равно 0')
else:
    b = {i:(1+1/i)**i for i in range(1,n+1)} #простите, очень хотелось потренировать словарь
    print(b)
    sum = 0.0
    for i in range(1,n+1):
        sum=sum+float(b[i])
    print('Сумма чисел последовательности:', sum)