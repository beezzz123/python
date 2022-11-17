from random import randint
pointwin = 0
pointlose = 0
while True:
    coin = randint(1,2)
    number = randint(1,2)#int(input("выбери 1 или 2 "))
    if number == 1 or number == 2:
        if number == coin:
            pointwin += 1
            print("победа")
        else:
            pointlose += 1
            print("поражение")
        print("текущий счёт" , pointwin , ":", pointlose )
    else:
        print("выбери число 1 или 2")
        break