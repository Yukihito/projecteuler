from math import *
from lib import *


#print(sum_of_aliquot(284))

ans = 0
for i in range(1, 10000):
  print("processing : " + str(i))
  a = sum_of_aliquot(i)
  if i != a and i == sum_of_aliquot(a):
    ans += i
print ans
