from turtle import Turtle

align = "center"
font = ["Courier", 18, "normal"]
font_game_over = ["Courier", 36, "bold"]

class Score(Turtle):

    def __init__(self):
        '''function to create the subclass Score'''
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align = align, font = font)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} (High Score: {self.high_score})", align = align, font = font)

    def add_score(self):
        '''function to mark the score on the screen'''
        self.score += 1
        self.update()

    def reset(self):
        '''function to reset score'''
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     '''function to show that the game is over'''
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = align, font = font_game_over)

