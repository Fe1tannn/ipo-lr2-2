import math
n = int(input("Число школьников"))
k = int(input("Число яблок"))
b = k % n
i = math.floor(k / n)
print (b, i)