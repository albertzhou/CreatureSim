import pygame


class Creature:
    xPos = None
    yPos = None
    size = None
    speed = None # pixels per second

    def __init__(self, xPos, yPos, size, speed):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.speed = speed


    def moveCreatureRight(self):
        self.xPos = self.xPos + self.speed

    def moveCreatureLeft(self):
        self.xPos = self.xPos - self.speed

    def CreatureJump(self):
        x = 0

    def checkCollisions(self, world):
        for e in world.environmentList:
            if self.yPos + self.size < e.topCoord:
                return True
            else:
                return False

    def handleInput(self, eventKey):
        if eventKey == pygame.K_d:
            self.moveCreatureRight()
        elif eventKey == pygame.K_a:
            self.moveCreatureLeft()
        elif eventKey == pygame.K_SPACE:
            self.CreatureJump()
        else:
            x = 0