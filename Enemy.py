import Point, random

class Enemy:
    gravity = 3

    speed = None #pixels per second
    top_left = None
    bot_right = None
    x_size = None
    y_size = None

    def __init__(self, top_left, bot_right, speed):
        self.speed = speed
        self.top_left = top_left
        self.bot_right = bot_right

        self.x_size = bot_right.xCoord - top_left.xCoord
        self.y_size = bot_right.yCoord - top_left.yCoord

    def random_movement(self, world):
        command = random.randint(1, 4)
        if command == 1:
            self.moveCreatureRight(world)
        elif command == 2:
            self.moveCreatureLeft(world)
        elif command == 3:
            self.CreatureJump(world)
        elif command == 4:
            self.CreatureFall(world)

        #shared with creature class:
    def moveCreatureRight(self, world):
        new_topleft = Point.Point(self.top_left.xCoord + self.speed, self.top_left.yCoord)
        new_botright = Point.Point(self.bot_right.xCoord + self.speed, self.bot_right.yCoord)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def moveCreatureLeft(self, world):
        new_topleft = Point.Point(self.top_left.xCoord - self.speed, self.top_left.yCoord)
        new_botright = Point.Point(self.bot_right.xCoord - self.speed, self.bot_right.yCoord)
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def applyGravity(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord + Enemy.gravity)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord + Enemy.gravity)
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def CreatureJump(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord - self.speed / 0.5)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord - self.speed / 0.5)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def CreatureFall(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord + self.speed)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord + self.speed)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def __overlap(self, l1, r1, l2, r2):
        if l1.xCoord > r2.xCoord or l2.xCoord > r1.xCoord:
            return False
        if l1.yCoord > r2.yCoord or l2.yCoord > r1.yCoord:  # swapped because y is inverted
            return False
        return True

        # returns true if desired x,y position intersects with an environment

    def __checkMoveValidity(self, new_topleft, new_botright, world):
        validity = True
        for e in world.environmentList:
            e_top_left = e.top_left
            e_bot_right = e.bot_right
            if Enemy.__overlap(None, e_top_left, e_bot_right, new_topleft, new_botright):
                validity = False
        return validity

        # returns a point with the creature's center location (to calculate projectile angles)

    def center(self):
        x_center = self.top_left.xCoord + round((self.bot_right.xCoord - self.top_left.xCoord) / 2)
        y_center = self.top_left.yCoord + round((self.bot_right.yCoord - self.top_left.yCoord) / 2)

        return Point.Point(x_center, y_center)