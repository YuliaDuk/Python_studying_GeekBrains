# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int,input('Введите последовательность чисел через пробел: ').split()))
print('Исходная последовательность:', numbers)
def uniquenum(numbers):
    newnumbers = []
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) == 1:
            newnumbers.append(numbers[i])
    return newnumbers
print('Неповторяющиеся элементы последовательности: ', uniquenum(numbers))
