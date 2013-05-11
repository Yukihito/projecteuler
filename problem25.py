n = 1
m = 1

i = 2

while True:
  i += 1
  l = n + m
  m = n
  n = l
  #print str(i) + " : " + str(n)
  if len(str(n)) == 1000:
    print i
    exit()
