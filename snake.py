import turtle
import time
import random

# Game settings
delay = 0.1
current_score = 0
best_score = 0

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game by @TokyoEdTech")
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates

# Snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("black")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Food
food_item = turtle.Turtle()
food_item.speed(0)
food_item.shape("circle")
food_item.color("red")
food_item.penup()
food_item.goto(0, 100)

# Snake body segments
snake_body = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement functions
def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def update_position():
    if snake_head.direction == "up":
        snake_head.sety(snake_head.ycor() + 20)
    elif snake_head.direction == "down":
        snake_head.sety(snake_head.ycor() - 20)
    elif snake_head.direction == "left":
        snake_head.setx(snake_head.xcor() - 20)
    elif snake_head.direction == "right":
        snake_head.setx(snake_head.xcor() + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Game loop
while True:
    screen.update()

    # Check for collisions with the wall
    if abs(snake_head.xcor()) > 290 or abs(snake_head.ycor()) > 290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        
        # Remove body segments
        for segment in snake_body:
            segment.goto(1000, 1000)
        snake_body.clear()
        
        current_score = 0
        delay = 0.1
        
        score_display.clear()
        score_display.write(f"Score: {current_score}  High Score: {best_score}", align="center", font=("Courier", 24, "normal"))

    # Detect collision with food
    if snake_head.distance(food_item) < 20:
        food_item.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        snake_body.append(new_segment)

        # Update delay and score
        delay -= 0.001
        current_score += 10

        if current_score > best_score:
            best_score = current_score
        
        score_display.clear()
        score_display.write(f"Score: {current_score}  High Score: {best_score}", align="center", font=("Courier", 24, "normal"))

    # Move body segments
    for index in range(len(snake_body) - 1, 0, -1):
        x, y = snake_body[index - 1].pos()
        snake_body[index].goto(x, y)

    if snake_body:
        snake_body[0].goto(snake_head.pos())

    update_position()

    # Check for collision with own body
    for segment in snake_body:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            
            for segment in snake_body:
                segment.goto(1000, 1000)
            snake_body.clear()

            current_score = 0
            delay = 0.1
            
            score_display.clear()
            score_display.write(f"Score: {current_score}  High Score: {best_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

screen.mainloop()
