# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите степень многочлена: '))
result = ''
for i in range(k,0,-1):
    a = '*x^'+ str(i)
    result +=(str(random.randint(0,100)) + a+ ' + ')
polinomial = result + str(random.randint(0,100)) + '= 0'
data = open('polinomial.txt', 'w')
data.writelines(polinomial)
data.close()