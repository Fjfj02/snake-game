#for this project, it can be provided a restart button to improve the user experience

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game") #create the screen for the game

snake = Snake()
food = Food()
score = Score() #create the "characters"

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right") #keybinds

game_on = True

while game_on: #game running
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15: #detect colision with food
        food.refresh()
        snake.extend()
        score.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: #detect colision with wall
        game_on = False
        score.game_over()

    for part in snake.allparts[1:]: #detect colision with body
        if snake.head.distance(part) < 10:
            game_on = False
            score.game_over()
        

screen.exitonclick()


