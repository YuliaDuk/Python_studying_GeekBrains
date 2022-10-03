# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def numberinbin(number):
    if number == 0:
        return []
    else:
        res = numberinbin(number//2)
        res.append(number%2)
        return res
number = int(input('Введите число: '))
print('Число в двоичной системе: ', "".join(map(str,numberinbin(number))))


    
    

