i = 32
found = False
while not found:
    if i % 10 == 0 and i % 100 == 0 and i % 87 == 0:
        print(i)
        found = True
    else:
        i += 1 