from math import *

def is_prime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  i = 3
  max_i = int(sqrt(num))
  while i <= max_i:
    if num % i == 0:
      return False
    i += 2
  return True


def last(arr):
  return arr[len(arr) - 1]

def extend_primes(num, primes):
  if last(primes) > num:
    return primes

  test = last(primes) + 1
  while True:
    if is_prime(test):
      primes.append(test)
      if test > num:
        return primes
    test += 1
  raise BaseException()

def insert(elem, pairs):
  for i in range(len(pairs)):
    if pairs[i][0] == elem:
      pairs[i][1] += 1
      return pairs
  pairs.append([elem, 1])
  return pairs

#def factorize(num, primes):
#  result = []
# 
#  primes = extend_primes(num, primes)
#  while True:
#    if num == 1:
#      break
#    for i in range(len(primes)):
#      if num % primes[i] == 0:
#        result = insert(primes[i], result)
#        num /= primes[i]
#        break
#  return result

def factorize(num, primes):
  result = []
  if is_prime(num):
    if num == 28:
      raise BaseException()
    result = insert(num, result)
    return result
  while True:
    if num == 1:
      break
    for i in range(2, int(sqrt(num))+1):
      if num % i == 0 and is_prime(i):
        result = insert(i, result)
        num /= i
        if num == i or is_prime(num):
          result = insert(num, result)
          num = 1
        break
  return result

def count_divisor(pairs):
  count = 1
  for i in range(len(pairs)):
    count *= pairs[i][1] + 1
  return count

def check_pairs(pairs):
  for i in range(len(pairs)):
    print(str(pairs[i][0]) + " : " + str(pairs[i][1]))
#check_pairs(factorize(28, [2]))
#print(count_divisor(factorize(28, [2])))

def sum_of_aliquot(n):
  factors = factorize(n, [2])
  result = 1
  for i in range(len(factors)):
    f_sum = 1
    for j in range(factors[i][1]):
      add_n = 1
      for k in range(j + 1):
        add_n *= factors[i][0]
      f_sum += add_n
    result *= f_sum
  result -= n
  return result
