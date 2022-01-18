from turtle import Turtle

# COLORS = ['red', 'blue', 'green']
# x_cor = -367
# Y = 230
# color_code = 0
COLORS = ['red', 'blue', 'green', 'yellow', 'cyan']


class Blocks:
    def __init__(self):
        super().__init__()
        self.all_blocks = []
        x = -367
        y = 230
        for j in range(5):
            for i in range(13):
                new_block = Turtle('square')
                new_block.penup()
                new_block.turtlesize(1.5, 2.7)
                new_block.color(COLORS[j])
                new_block.goto(x, y)
                x += 60
                self.all_blocks.append(new_block)
            x = self.all_blocks[0].xcor()
            y -= 35






