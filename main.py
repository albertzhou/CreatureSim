import pygame, sys, Wall, Point, Enemy
import World, Creature
import pygame.locals


class main:

    #Colors in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)

    Origin = Point.Point(0, 0)

    if __name__ == "__main__":
        pygame.init()

        ## Spawn player, floors, and wall
        gameWorld = World.World(500, 500)
        gameWorld.initialize_world()
        player = Creature.Creature(Point.Point(250, 400), Point.Point(275, 425), 5)  # xloc, yloc, size
        gameWorld.spawnCreature(player)
        floor = Wall.Wall(Point.Point(0, gameWorld.yPixels - 30), Point.Point(gameWorld.xPixels, gameWorld.yPixels))
        leftWall = Wall.Wall(Origin, Point.Point(30, gameWorld.yPixels))
        rightWall = Wall.Wall(Point.Point(gameWorld.xPixels - 30, 0), Point.Point(gameWorld.yPixels, gameWorld.yPixels))
        ceiling = Wall.Wall(Origin, Point.Point(gameWorld.xPixels, 30))
        gameWorld.spawnWall(floor)
        gameWorld.spawnWall(leftWall)
        gameWorld.spawnWall(rightWall)
        gameWorld.spawnWall(ceiling)
        gameWorld.updateWorld()
        ## end world initialization

        ## spawn enemy
        en1 = Enemy.Enemy(Point.Point(300, 300), (Point.Point(325, 325)), 5, 100)
        gameWorld.spawn_enemy(en1)


        while True: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.locals.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    player.handleMouseClick(pos, gameWorld)
            keys = pygame.key.get_pressed()  # checking pressed keys
            player.handleInput(keys, gameWorld)
            gameWorld.screen.fill(BLACK)
            gameWorld.updateWorld()  # update all locations
            gameWorld.renderworld()  # redraw the world on screen
