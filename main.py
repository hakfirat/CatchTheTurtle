import turtle
import random
import time

def score(x, y):
    global counter
    counter += 1
    target.speed(0)
    target.goto(random.randint(-250, 250), random.randint(-250, 250))
    update_score

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {counter}", align="center", font=("Verdana", 16, "bold"))
    time_pen.clear()
    time_pen.write(f"Time: {time_left}", align="center", font=("Verdana", 16, "bold"))

def timer():
    global time_left
    time_left -= 1
    if time_left > 0:
        update_score()
        screen.ontimer(timer, 1000)
    else:
        score_pen.clear()
        time_pen.clear()
        score_pen.write(f"Score: {counter}", align="center", font=("Verdana", 16, "bold"))
        time_pen.write(f"Game Over!", align="center", font=("Verdana", 16, "bold"))
        target.hideturtle()


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
screen.setup( width=1200, height=800)

target = turtle.Turtle()
target.speed(0)
target.shape("turtle")
target.shapesize(2)
target.color("green")
target.penup()
target.goto(random.randint(-250, 250), random.randint(-250, 250))
target.onclick(score)

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("blue")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 340)
score_pen.write("Score: 0", align="center", font=("Verdana", 16, "bold"))

time_pen = turtle.Turtle()
time_pen.speed(0)
time_pen.color("black")
time_pen.penup()
time_pen.hideturtle()
time_pen.goto(0, 300)
time_pen.write("Time: 10", align="center", font=("Verdana", 16, "bold"))

time_limit = 10
time_left = time_limit
counter = 0

screen.ontimer(timer, 1000)

turtle.mainloop()
