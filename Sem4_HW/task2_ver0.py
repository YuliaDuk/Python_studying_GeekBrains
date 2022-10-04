# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from sympy import *

n = int(input('Введите натуральное число: '))

def is_primenum(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
            
listofmultipl = []
if n>0:
    for i in range(2,n):
        if is_primenum(i) == True:                         #isprime(i) == True:
            if n%i == 0:
                listofmultipl.append(i)
    print('Список множителей: ', listofmultipl)
else:
    print('Введите другое число')


