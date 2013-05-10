from math import *
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
count = 0
while True:
  if is_prime(i):
    count += 1
    if count == 10001:
      print(i)
      break
  i += 1
