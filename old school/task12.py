def triangle(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        print("выйдет")
    else:
        print("не выйдет")


a = 6
b = 18
c = 6
triangle(5,6,8)