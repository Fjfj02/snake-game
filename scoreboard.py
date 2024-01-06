from turtle import Turtle

align = "center"
font = ["Courier", 18, "normal"]
font_game_over = ["Courier", 36, "bold"]

class Score(Turtle):

    def __init__(self):
        '''function to create the subclass Score'''
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align = align, font = font)
        self.hideturtle()

    def add_score(self):
        '''function to mark the score on the screen'''
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = align, font = font)

    def game_over(self):
        '''function to show that the game is over'''
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align = align, font = font_game_over)

