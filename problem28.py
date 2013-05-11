length = 3
pos = 3
result = 1
max_length = 1001
while length <= max_length:
  for i in range(4):
    #print str(length) + " : " + str(pos)
    result += pos
    if i != 3:
      pos += (length - 1)
  length += 2
  pos += (length - 1)
print result
