from turtle import Turtle

snake_starting_positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:

    def __init__(self):
        '''initial function'''
        self.allparts = []
        self.create_snake()
        self.head = self.allparts[0]

    def create_snake(self):
        '''function to create the snake'''
        for position in snake_starting_positions:
            self.add_part(position)

    def add_part(self, position):
        part_snake = Turtle("square")
        part_snake.color("white")
        part_snake.penup()
        part_snake.goto(position)
        self.allparts.append(part_snake)

    def extend(self):
        self.add_part(self.allparts[-1].position())

    def move(self):
        '''function to move the snake'''
        for part in range(len(self.allparts) - 1, 0, -1):
            x = self.allparts[part - 1].xcor()
            y = self.allparts[part - 1].ycor()
            self.allparts[part].goto(x, y)
        self.allparts[0].forward(move_distance)

    def up(self):
        '''function to go up'''
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        '''function to go down'''
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        '''function to go left'''
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        '''function to go right'''
        if self.head.heading() != left:
            self.head.setheading(right)