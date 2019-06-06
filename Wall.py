import Point


class Wall:
    top_left = None
    bot_right = None
    x_size = None
    y_size = None

    def __init__(self, top_left, bot_right):
        self.top_left = top_left
        self.bot_right = bot_right

        self.x_size = bot_right.xCoord - top_left.xCoord
        self.y_size = bot_right.yCoord - top_left.yCoord