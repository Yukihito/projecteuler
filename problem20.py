n = 1
for i in range(2, 101):
  n *= i

s = str(n)

r = 0
for i in range(len(s)):
  r += int(s[i])

print(r)
