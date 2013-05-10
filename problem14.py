def is_even(n):
  return n % 2 == 0
def collatz_count(n):
  count = 0
  while n != 1:
    if is_even(n):
      n = n/2
    else:
      n = 3*n + 1
    count += 1
  return count

winner = -1
winner_count = -1
for i in range(1, 1000000):
  print("processing : " + str(i))
  count = collatz_count(i)
  if count > winner_count:
    winner_count = count
    winner = i
print(str(winner))
