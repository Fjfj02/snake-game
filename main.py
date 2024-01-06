from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game") #create the screen for the game

snake_starting_positions = [(0,0), (-20,0), (-40,0)]
allparts = []

for position in snake_starting_positions: #create the snake
    part_snake = Turtle("square")
    part_snake.color("white")
    part_snake.penup()
    part_snake.goto(position)
    allparts.append(part_snake)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for part in range(len(allparts) - 1, 0, -1):
        x = allparts[part - 1].xcor()
        y = allparts[part - 1].ycor()
        allparts[part].goto(x, y)
    allparts[0].forward(20)


screen.exitonclick()


