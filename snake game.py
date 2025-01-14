import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Let's creart a window screen for the gameplay.
window_screen = turtle.Screen()
window_screen.title("Snake world")
window_screen.bgcolor("#000")
window_screen.setup(width=600, height=600)
window_screen.tracer()

# Let's creat the head of the snake.
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("yellow")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Let's creat the food for the snake.
snake_food = turtle.Turtle()
colors = random.choice(['#11f005']) # you can add different color for the food.
shapes = random.choice(['circle']) # you can add different shape of the food.
snake_food.speed(0)
snake_food.shape(shapes)
snake_food.color(colors)
snake_food.penup()
snake_food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("#f05705")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0",align="center",font=("san-serif",30,"bold"))

# Let's assaign keys for the direction of the snake.
def up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

window_screen.listen()
window_screen.onkeypress(up, "w")
window_screen.onkeypress(down, "s")
window_screen.onkeypress(left, "a")
window_screen.onkeypress(right, "d")

snake_length = []

# Let's create the gameplay for the snake.
while True:
    window_screen.update()
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"
        colors = random.choice(['red','blue','green'])
        shapes = random.choice(['square', 'circle'])
        for length in snake_length:
            length.goto(1000, 1000)
        snake_length.clear()
        Score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score),align="center", font=("san-serif",30,"bold"))
    if snake_head.distance(snake_food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        snake_food.goto(x,y)

        # Let's add the  length segment for the snake body.
        new_length = turtle.Turtle()
        new_length.speed(0)
        new_length.shape("square")
        new_length.color("orange")
        new_length.penup()
        snake_length.append(new_length)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score,high_score),align="center", font=("san-serif",30,"bold"))

    # If head strike with the body.
    for index in range(len(snake_length) -1, 0, -1):
        x = snake_length[index - 1].xcor()
        y = snake_length[index - 1].ycor()
        snake_length[index].goto(x,y)
    if len(snake_length) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_length[0].goto(x, y)
    move()
    for length in snake_length:
        if length.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            colors = random.choice(['red','blue','green'])
            shapes = random.choice(['square','circle'])
            for length in snake_length:
                length.goto(1000, 1000)
            length.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.wwrite("Score : {} High Score : {}".format(score,high_score),align="center", font=("san-serif",30,"bold"))
    time.sleep(delay)

window_screen.mainloop()