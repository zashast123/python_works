# import random
# import random as r
#
# # from random import  randint
# # from random import * # так лучше не делать
# x = r.randint(0, 100)  # от 0 до 100
# lst = [0, 1, 2, 3, 4, 5]
# r.shuffle(lst) #shuffle- перемешать
# element_random = r.choice(lst) #выбрать
# r.shuffle(lst)
#
# print(x)
# print(lst)
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(-300,250)
t.pendown()
screen = turtle.Screen()
t.color("dark green","pink")
t.pensize(5)
t.speed(1)
goriont = 300
vertical =200
t.begin_fill()
t.forward(goriont)  #вперед на 50 пикселей
t.right(90)    #поворот на право
t.forward(vertical)  #вперед на 50 пикселей
t.right(90)    #поворот на право
t.forward(goriont)  #вперед на 50 пикселей
t.right(90)    #поворот на право
t.forward(vertical)  #вперед на 50 пикселей
t.right(90)    #поворот на право
t.end_fill()
t.penup()
t.goto(-100,200)
t.pendown()
t.fd(50)

t.write("Movavi", font=("Arial Black",50,"normal"),align="center")
screen.exitonclick()
