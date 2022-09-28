#Реализуйте алгоритм перемешивания списка
from random import randint
def mixlist (list):
    for i in range(len(list)):
        a = list[i]
        index = randint(0, len(list)-1)
        list[i] = list[index]
        list[index] = a
    return list

n = int(input('Введите число элементов списка: '))
listold = []
for i in range(n):
    listold.append(randint(0,10))
print('Исходный список', listold)
print('Список после перемешивания: ', mixlist(listold))
