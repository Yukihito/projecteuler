max_index = 1000000

def sorted_sequences(left_nums, product):
  if len(left_nums) == 1:
    return [product + str(left_nums[0])]
  sequences = []
  for i in range(len(left_nums)):
    l = left_nums[:]
    c = l.pop(i)
    sequences.extend(sorted_sequences(l, product + str(c)))
  return sequences

sequences = sorted_sequences([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "")

for s in sequences:
  print s
print(sequences[max_index])
print(sequences[max_index-1])
