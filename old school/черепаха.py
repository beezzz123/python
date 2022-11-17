import turtle
io = turtle.Pen()
io.width(4)
io.color("red")
for i in range(1,360):
    io.right(i*47)
    for j in range(15):
        io.right(8*i)
        io.forward(j*i)
        io.width(i % 180)
        if i > 180:
            io.color("purple")




number = input()