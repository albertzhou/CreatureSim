import pygame


class Creature:
    xPos = None
    yPos = None
    size = None
    speed = None #pixels per second

    leftCoord = None
    rightCoord = None
    topCoord = None
    botCoord = None

    def __init__(self, xPos, yPos, size, speed):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.speed = speed

        self.leftCoord = self.xPos
        self.rightCoord = self.xPos + self.size
        self.topCoord = self.yPos
        self.botCoord = self.yPos + self.size

    def moveCreatureRight(self, world):
        if self.ccRight(world):
            self.xPos = self.xPos + self.speed

    def moveCreatureLeft(self, world):
        if self.ccLeft(world):
            self.xPos = self.xPos - self.speed

    def CreatureJump(self, world):
        x = 0

    def ccBot(self, world): # check collisions bot -- returns true if there is a collision
        for e in world.environmentList:
            if self.yPos + self.size < e.topCoord:
                return True
        return False

    def ccRight(self, world):
        for e in world.environmentList:
            if self.xPos + self.size < e.leftCoord:
                return True
        return False

    def ccLeft(self, world):
        for e in world.environmentList:
            if self.xPos < e.rightCoord:
                return True
        return False

    def handleInput(self, eventKey, world):
        if eventKey == pygame.K_d:
            self.moveCreatureRight(world)
        elif eventKey == pygame.K_a:
            self.moveCreatureLeft(world)
        elif eventKey == pygame.K_SPACE:
            self.CreatureJump(world)
        else:
            x = 0