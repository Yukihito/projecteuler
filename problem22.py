def get_char_score(char):
  return ord(char) - 64

def get_string_score(string):
  score = 0
  for i in range(len(string)):
    score += get_char_score(string[i])
  return score

print get_string_score("COLIN")

f = open("names.txt", 'r')
file_content = ""
for line in f:
  file_content = file_content + line
f.close()

names = file_content.split(",")

for i in range(len(names)):
  names[i] = names[i].replace('"', "")

def name_sort_rule(x, y):
  i = 0
  while i < len(x) and i < len(y):
    if get_char_score(x[i]) < get_char_score(y[i]):
      return -1
    elif get_char_score(x[i]) > get_char_score(y[i]):
      return 1
    i += 1
  return len(x) - len(y)
names = sorted(names, cmp=name_sort_rule)
result = 0
for i in range(len(names)):
  r = (1 + i) * get_string_score(names[i])
  result += r
  print(str(i) + " : " + names[i] + " : " + str(r))
print(result)
