import turtle
turtle.bgcolor("white")
turtle.pensize(2.5)
turtle.speed(0.2)
color=["red","blue","green","orange"]
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.right(10)
turtle.mainloop()
