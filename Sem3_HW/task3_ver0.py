# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import math
numbers = list(input('Введите числа через запятую: ').split(','))
min = math.inf
max = 0
for i in range(len(numbers)):
    if ('.') in str(numbers[i]):        
        if float(('0.'+ str(numbers[i]).split('.')[1])) > max:
            max = float('0.'+str(numbers[i]).split('.')[1])
        elif float('0.'+ str(numbers[i]).split('.')[1]) < min:
            min = float('0.'+ str(numbers[i]).split('.')[1])
print('Исходный список: ', numbers)
print('Максмальное значение дробной части: ', max)
print('Минимальное значение дробной части: ', min)
print('Разница: ', max-min)

