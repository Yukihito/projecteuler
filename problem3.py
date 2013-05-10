from math import *
num = 600851475143
result = 2
def is_prime(num):
  if num == 1:
    return False
  if num == 2:
    return True
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True
i = 2
while True:
  if num == 1:
    break
  if num % i == 0:# and is_prime(i):
    result = i
    num /= i
  i += 1

print result
