import pygame


class World:
    #Colors in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 200,   150)
    RED =   (255,   0,   0)

    xPixels = 500 # size of world in pixels
    yPixels = 500

    xGridSize = None # grid size of the world
    yGridSize = None
    screen = None

    creatureList = []
    environmentList = []

    def __init__(self, x, y):
        self.xgridsize = x
        self.ygridsize = y

    def makeworld(self, x, y):
        world = World(x, y)
        return world

    def initializeworld(self):
        screen = pygame.display.set_mode((self.xPixels, self.yPixels))
        self.screen = screen
        pygame.display.set_caption('Creature Simulator')
        pygame.display.flip()

    def renderworld(self):
        pygame.display.flip()

    def spawnCreature(self, c):
        self.creatureList.append(c)

    def spawnWall(self, e):
        self.environmentList.append(e)

    def updateWorld(self):
        for c in self.creatureList:
            if c.checkCollisions(self):
                c.yPos += 1 # effect of gravity in pixels per loop
            pygame.draw.rect(self.screen, (128, 128, 0), pygame.Rect(c.xPos, c.yPos, c.size, c.size))
        for e in self.environmentList:
            pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(e.xPos, e.yPos, e.xSize, e.ySize))
