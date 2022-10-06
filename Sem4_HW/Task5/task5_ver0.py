# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
from numpy.polynomial import Polynomial as P

path = 'firstpolynomial.txt'
data = open(path, 'r')
for line in data:
    polynom1 = line
print(polynom1)
data.close()
path = 'secondpolynomial.txt'
data = open(path, 'r')
for line in data:
    polynom2 = line
print(polynom2)
data.close()

def koeffofdeg(polynom):
    polynom = polynom.replace('-','+ -')
    monomlist = list(map(str,polynom.split('+')))
    koeff = []
    for i in range(len(monomlist)):
        if monomlist[i].count('x')==0:
            koeff.append(int(0))
        else:
            koeff.append(int(monomlist[i][monomlist[i].find('^')+1:]))
    max_degree = max(koeff)
    return max_degree

def koeffofpolyn(polynom, maxdeg):
    polynom = polynom.replace('-','+ -')
    monomlist = list(map(str,polynom.split('+')))
    koeff = [0]*(maxdeg+1)
    index =0
    diff = maxdeg - len(monomlist)
    for i in range(maxdeg,-1,-1):
        if monomlist[index].count('x') == 0:
            koeff[i] = int(monomlist[index])
        else:
            koeff[i]=int(monomlist[index][:monomlist[index].find('*')])
        index+=1
    return koeff
    
max_degree1 = koeffofdeg(polynom1)
max_degree2 = koeffofdeg(polynom2)

p1 = P(koeffofpolyn(polynom1,max_degree1))
p2 = P(koeffofpolyn(polynom2,max_degree2))

print(p1 + p2)

data = open('finalpolynomial.txt', 'w')
data.writelines(str(p1+p2))
data.close()