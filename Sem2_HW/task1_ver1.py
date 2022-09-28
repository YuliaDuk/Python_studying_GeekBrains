#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

string = input('Введите число: ')
newstring = string.replace('-', '0').replace('.', '0')
sum =0
for i in range(len(newstring)):
    sum+=int(newstring[i])
print('Сумма цифр числа равна', sum)