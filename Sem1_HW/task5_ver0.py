# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1y1 = list(map(float,input('Введите координаты первой точки через запятую: ').split(',')))
x2y2 = list(map(float,input('Введите координаты второй точки через запятую: ').split(',')))
distance = ((x2y2[0]-x1y1[0])**2 + (x2y2[1]-x1y1[1])**2)**0.5
print(distance)