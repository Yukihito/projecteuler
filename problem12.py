from math import *
from lib import *

#def count_div(num):
#  count = 0
#  pair_num = num
#  for i in range(num):
#    test_num = i + 1
#    if num % test_num == 0:
#      pair_num = num / test_num
#      if test_num == pair_num:
#        count += 1
#        break
#      elif test_num > pair_num:
#        break
#      else:
#        count += 2
#  return count

def problem():
  i = 1
  tri_num = 1
  primes = [2]
  while True:
    count = count_divisor(factorize(tri_num, primes))
    #print(str(i) + " : " + str(count))
    if count >= 500:
      print tri_num
      exit()
    i += 1
    tri_num += i
problem()

