c = 997
while True:
  a_plus_b = 1000 - c
  a = 1
  b = a_plus_b - a
  while a < b:
    if b >= c:
      pass
    elif a * a + b * b == c * c:
      print a * b * c
      exit(0)
    a += 1
    b -= 1
  c -= 1
