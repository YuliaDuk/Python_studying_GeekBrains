#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

string = input('Введите число: ')
newstring = ''
for i in range(0, len(string)):
    if string[i] != '.' and string[i] != '-':
        newstring += string[i]
sum = 0
for i in range(len(newstring)):
    sum += int(newstring[i])
print("Сумма цифр числа", string, "равна", sum)

