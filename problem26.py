def calc_repet_length(m):
  while True:
    if m % 2 == 0:
      m /= 2
    elif m % 5 == 0:
      m /= 5
    elif m == 1:
      return 0
    else:
      break
  a = 1
  while True:
    if pow(10, a) % m == 1:
      return a
    a += 1

winner_index = -1
winner_value = -1
for i in range(2, 1001):
  print "processing : " + str(i)
  test = calc_repet_length(i)
  if test > winner_value:
    winner_value = test
    winner_index = i
print(winner_index)
