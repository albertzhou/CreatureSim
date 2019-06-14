import pygame, random, Enemy, Point, Wall


class World:
    #Colors in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 200,   150)
    RED =   (255,   0,   0)
    ENEMY_RED = (255, 120, 0)

    xPixels = 500 # size of world in pixels
    yPixels = 500

    xGridSize = None # grid size of the world
    yGridSize = None
    screen = None

    gravity = 10  # gravity in pixels per second

    creatureList = []
    environmentList = []
    projectileList = []
    enemy_list = []

    def __init__(self, x, y):
        self.xgridsize = x
        self.ygridsize = y

    def initialize_world(self):
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

    def spawn_projectile(self, b):
        self.projectileList.append(b)

    def spawn_enemy(self, en):
        self.enemy_list.append(en)

    # removes projectile from memory if it is off screen
    def clear_old_projectiles(self, p):
        if p.x_pos > self.xPixels or p.y_pos > self.yPixels:
            self.projectileList.remove(p)
        elif p.x_pos < 0 or p.y_pos < 0:
            self.projectileList.remove(p)

    def updateWorld(self):
        for c in self.creatureList: #update creature positions
            c.applyGravity(self)
            pygame.draw.rect(self.screen, (128, 128, 0), pygame.Rect(c.top_left.xCoord, c.top_left.yCoord, c.x_size, c.y_size))
        for en in self.enemy_list:
            if en.health < 0:
                self.enemy_list.remove(en)
            else:
                en.random_movement(self)
                pygame.draw.rect(self.screen, en.color, pygame.Rect(en.top_left.xCoord, en.top_left.yCoord, en.x_size, en.y_size))
        for e in self.environmentList: #update environment positions
            pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(e.top_left.xCoord, e.top_left.yCoord, e.x_size, e.y_size))
        for p in self.projectileList: #update projectile positions
            p.update_position()
            p.apply_damage(self)
            p.absorb_projectile(self)
            self.clear_old_projectiles(p)
            pygame.draw.circle(self.screen, self.RED, [int(p.x_pos), int(p.y_pos)], p.size)

        # spawn more creatures randomly if there are fewer than a certain number of creatures
        if len(self.enemy_list) < 3:
            x_pos = random.randint(30, self.xPixels - 80)
            y_pos = random.randint(30, self.yPixels - 80)
            size = random.randint(25, 45)
            speed = random.randint(3, 10)
            health = random.randint(30, 80)
            en = Enemy.Enemy(Point.Point(x_pos, y_pos), (Point.Point(x_pos + size, y_pos + size)), speed, health)
            self.spawn_enemy(en)

            x_pos_tl = random.randint(100, 400) # top left coords
            y_pos_tl = random.randint(100, 400)

            x_pos_br = random.randint(x_pos_tl, 470)
            y_pos_br = random.randint(y_pos_tl, 470)

            # e = Wall.Wall()
