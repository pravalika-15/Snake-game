from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
snake = Snake()
screen = Screen()
food = Food()
scoreboard = ScoreBoard()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width = 600, height = 600)

starting_position = [(0,0), (-20,0), (-40,0)]
segments = []


screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    for segment in segments:
        if snake.head.distance(segment[1:]) < 10:
            snake.reset()
            scoreboard.reset()


screen.exitonclick()