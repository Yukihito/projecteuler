n = 2
for i in range(2, 1001):
  n *= 2

s = str(n)
result = 0
for i in range(len(s)):
  result += int(s[i])
print(result)
