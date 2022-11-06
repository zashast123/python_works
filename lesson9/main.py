import random
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(7)
colors = ["red","orange","yellow","green", "light blue", "blue","purple"]
side = int(input("Введите кол-во сторон:"))
x = 80
for i in range(0,side):
    t.pencolor(random.choicei(colors))
    t.fd(x)
    t.rt(360 / side)




screen.exitonclick()