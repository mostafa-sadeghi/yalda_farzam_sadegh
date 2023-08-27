from turtle import Screen, Turtle
import random
from time import sleep


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


main_surface = Screen()
main_surface.bgcolor('black')
main_surface.setup(600, 600)
main_surface.title("Snake Game")

main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")


def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    x = random.randint(-270, 270)
    y = random.randint(-270, 230)
    object.goto(x, y)


snake_head = create_turtle("square", "blue")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")

change_position(snake_food)

score = 0

scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()


snake_tails = []
main_surface.tracer(False)
running = True
while running:
    main_surface.update()
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", align="center", font=("arial", 22))
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        score += 1

        new_tail = create_turtle("square", "blue")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        score = 0
        snake_head.goto(0, 0)
        snake_head.direction = ""
        for tail in snake_tails:
            tail.ht()
        snake_tails.clear()

    # TODO  یک کاراکتر مخرب به بازی اضافه کنید و در صورت برخورد مار با آن یک امتیاز از بازیکن کم شود و نیز
    # یکی از طول مار هم کم شود

    move_snake()
    sleep(0.2)
