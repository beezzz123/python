k = 2
m = 5
n = 21312
time = m * 2 
if n % k == 0:
  answer = (n // k) * time
else:
   answer = (n // k + 1) * time
if answer > 60:
    print(answer  // 60, " Часов ", answer % 60, " Минут")
else:
    print( answer, " Минут")
