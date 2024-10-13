from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

user_level = screen.textinput(title="Choose your Difficulty", prompt="Easy/Medium/Hard: ")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    if user_level.lower() == "easy":
        time.sleep(0.1)
    elif user_level.lower() == "medium":
        time.sleep(0.08)
    else:
        time.sleep(0.05)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_turt()
        scoreboard.increase_score()
        scoreboard.update_score()

    for segment in snake.turts[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

screen.exitonclick()