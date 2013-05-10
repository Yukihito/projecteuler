a = 0

for i in range(100):
  num = i + 1
  a += num * num

b = 0

for i in range(100):
  num = i + 1
  b += num

b = b * b

print(a - b)
