import pygame, sys, Wall
import World, Creature
import pygame.locals


class main:

    #Colors in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)

    if __name__ == "__main__":
        pygame.init()

        ## Spawn player and floor
        gameWorld = World.World(500, 500)
        gameWorld.initializeworld()
        player = Creature.Creature(50, 50, 25, 10)  # xloc, yloc, size
        gameWorld.spawnCreature(player)
        floor = Wall.Wall(0, gameWorld.yPixels - 30, gameWorld.yPixels, 30)
        leftWall = Wall.Wall(0, 0, 30, gameWorld.yPixels)
        rightWall = Wall.Wall(gameWorld.xPixels - 30, 0, 30, gameWorld.yPixels)
        gameWorld.spawnWall(floor)
        gameWorld.spawnWall(leftWall)
        gameWorld.spawnWall(rightWall)
        gameWorld.updateWorld()

        while True: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    eventKey = event.key
                    player.handleInput(eventKey, gameWorld)
                else:
                    x = 0
            gameWorld.screen.fill(BLACK)
            gameWorld.updateWorld()
            gameWorld.renderworld()

