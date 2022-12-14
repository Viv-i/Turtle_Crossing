from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.ht()
        self.penup()
        self.color('white')
        self.goto(-450, 350)
        self.write(f'Level: {self.score}', align='left', font=('Arial', 25, 'normal'))

    def add_level(self):
        self.score += 1
        self.clear()
        self.goto(-450, 350)
        self.write(f'Level: {self.score}', align='left', font=('Arial', 25, 'normal'))

    def game_over(self):
        g_over = Turtle()
        g_over.ht()
        g_over.penup()
        g_over.color('white')
        g_over.goto(0, 0)
        g_over.write(f"Game Over", align='center', font=('Arial', 25, 'normal'))
