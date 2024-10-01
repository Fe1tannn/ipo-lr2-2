import math
a = int(input("Введите длину a: "))
b = int(input("Введите длину b: "))
c = int(input("Введите длину c: "))
d = int(input("Введите длину d: "))
p = (a + b + c + d) / (2)
s = ((a + b) / math.fabs(a - b)) * math.sqrt(p - a) * (p - b) * (p - a - c) * (p - a - d)
print (s)