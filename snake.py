from turtle import Screen, Turtle
import random
main_surface = Screen()
main_surface.bgcolor('black')
main_surface.setup(600, 600)
main_surface.title("Snake Game")

def create_turtle(tshape, tcolor):
    my_turtle= Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle

# تابعی بنویسید که جای غذا را به صورت تصادفی در صفحه تغییر دهد
# یعنی غذای مار را به یک مکان تصادفی در صفحه منتقل نماید

snake_head = create_turtle("square", "blue")
snake_food = create_turtle("circle", "red")
snake_food.goto(0,100)


running = True
while running:
    main_surface.update()
