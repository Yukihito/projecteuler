from lib import *
from sets import Set
def is_abundant(n):
  return sum_of_aliquot(n) > n
abundants = []
for i in range(2, 28124):
  if is_abundant(i):
    abundants.append(i)
sums_set = Set([])
for i in abundants:
  print("progress : " + str(i) + "/" + str(len(abundants)))
  for j in abundants:
    sums_set.add(i + j)
result = 0
for i in range(1, 28124):
  print(i)
  if i not in sums_set:
    result += i
print result
