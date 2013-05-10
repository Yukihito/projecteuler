i = 20

while True:
  dividable = True
  for j in range(20):
    if i % (j + 1) != 0:
      dividable = False
      break
  if dividable:
    print(i)
    break
  i += 1
