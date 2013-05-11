from lib import *

class Quadric:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def calc(self, n):
    return n * n + self.a * n + self.b

winner = -1
winner_length = -1
for i in range(-999, 1000):
  print("processing : " + str(i + 999) + "/1999")
  for j in range(-999, 1000):
    quad = Quadric(i, j)
    for k in range(1000):
      if not is_prime(quad.calc(k)):
        if k > winner_length:
          winner_length = k
          winner = i * j
        break
print winner
