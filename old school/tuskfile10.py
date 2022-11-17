current = 1
parevious = 0
n = 100000
for i in range(1,n):
  print(current)
  tmp = current
  current = parevious + tmp
  parevious = tmp
