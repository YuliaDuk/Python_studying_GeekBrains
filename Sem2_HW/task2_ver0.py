# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
from math import factorial


n = int(input('Введите число N: '))
mass =[]
if n<=0:
    print('произведение чисел от 1 до N равно 0')
else:
    for i in range(1,n+1):
        mass.append(factorial(i))
    print('Набор произведений чисел от 1 до N', mass)