class Wall:
    xPos = None
    yPos = None
    xSize = None
    ySize = None

    topCoord = None

    def __init__(self, xpos, ypos, xsize, ysize):
        self.xPos = xpos
        self.yPos = ypos
        self.xSize = xsize
        self.ySize = ysize

        self.topCoord = self.yPos