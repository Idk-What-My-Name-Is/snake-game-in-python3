import turtle
import time
import random

#screen setup
wn = turtle.Screen()
wn.title("snake game")
wn.setup(width=600, height=600)
wn.bgcolor("green")
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 160)

tails = []

#functions
def go_up():
    y = head.ycor()
    head.penup()
    head.sety(y + 20)

def go_down():
    y = head.ycor()
    head.penup()
    head.sety(y - 20)

def go_right():
    x = head.xcor()
    head.penup()
    head.setx(x + 20)

def go_left():
    x = head.xcor()
    head.penup()
    head.setx(x - 20)


#keybinds
wn.listen()
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

#mainloop
while True:
    wn.update()

    # Check for collision with border
    if head.ycor() > 300 or head.ycor() < -300 or head.xcor() > 300 or head.xcor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    #check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,  y)
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("white")
        new_tail.penup()
        tails.append(new_tail)

    



