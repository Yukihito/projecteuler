b = 1
n = 2
c = 2
result = 2
while True:
  c = b + n
  if c > 4000000:
    break
  if c % 2 == 0:
    result += c
  b = n
  n = c
print result
