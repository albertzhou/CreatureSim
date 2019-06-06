import pygame, Point


class Creature:
    gravity = 1

    speed = None #pixels per second
    top_left = None
    bot_right = None
    x_size = None
    y_size = None

    def __init__(self, top_left, bot_right, speed):
        self.top_left = top_left
        self.bot_right = bot_right
        self.speed = speed

        self.x_size = bot_right.xCoord - top_left.xCoord
        self.y_size = bot_right.yCoord - top_left.yCoord

    def moveCreatureRight(self, world):
        new_topleft = Point.Point(self.top_left.xCoord + self.speed, self.top_left.yCoord)
        new_botright = Point.Point(self.bot_right.xCoord + self.speed, self.bot_right.yCoord)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright
            print("move right")
        print("could not move right")

    def moveCreatureLeft(self, world):
        new_topleft = 0
        new_botright = 0
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def applyGravity(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord + Creature.gravity)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord + Creature.gravity)
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright
            print("applied gravity")
        else:
            print("could not apply gravity")

    def CreatureJump(self, world):
        x = 0

    def handleInput(self, eventKey, world):
        if eventKey == pygame.K_d:
            self.moveCreatureRight(world)
        elif eventKey == pygame.K_a:
            self.moveCreatureLeft(world)
        elif eventKey == pygame.K_SPACE:
            self.CreatureJump(world)
        else:
            x = 0

    @staticmethod
    def __overlap(self, l1, r1, l2, r2):
        if l1.xCoord > r2.xCoord or l2.xCoord > r1.xCoord:
            return False
        if l1.yCoord < r2.yCoord or l2.yCoord < r1.yCoord:
            return False
        return True

    # returns true if desired x,y position intersects with an environment
    def __checkMoveValidity(self, new_topleft, new_botright, world):
        for e in world.environmentList:
            e_top_left = e.top_left
            e_bot_right = e.bot_right
            return not Creature.__overlap(None, e_top_left, e_bot_right, new_topleft, new_botright)