from math import *
max_num = 2000000

def is_prime(num):
  if num == 1:
    return False
  if num == 2:
    return True
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

result = 0
for i in range(max_num):
  test = i + 1
  if is_prime(test):
    result += test
print result
