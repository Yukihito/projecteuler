def is_palindrome_number(num):
  num_len = len(str(num))
  half_len = int(num_len/2)
  if float(num_len)/2 > half_len:
    half_len += 1
  strnum = str(num)
  for i in range(half_len):
    inv_i = num_len - i - 1
    if strnum[i] != strnum[inv_i]:
      return False
  return True


winner = -1
for i in range(999):
  for j in range(999):
    test = i * j
    if test > winner and is_palindrome_number(test):
      winner = test

print(winner)
