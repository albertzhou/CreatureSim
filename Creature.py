import pygame, Point, Projectile


class Creature():
    gravity = 3
    health = 100

    speed = None #pixels per second
    top_left = None
    bot_right = None
    x_size = None
    y_size = None
    consecutive_jumps = 0

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

    def moveCreatureLeft(self, world):
        new_topleft = Point.Point(self.top_left.xCoord - self.speed, self.top_left.yCoord)
        new_botright = Point.Point(self.bot_right.xCoord - self.speed, self.bot_right.yCoord)
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def applyGravity(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord + Creature.gravity)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord + Creature.gravity)
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

    def handleInput(self, keys, world):
        if keys[pygame.K_d] and (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            self.moveCreatureRight(world)
            self.CreatureJump(world)
        elif keys[pygame.K_a] and (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            self.moveCreatureLeft(world)
            self.CreatureJump(world)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.moveCreatureLeft(world)
            self.CreatureFall(world)
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.moveCreatureRight(world)
            self.CreatureFall(world)
        elif keys[pygame.K_d]:
            self.moveCreatureRight(world)
        elif keys[pygame.K_a]:
            self.moveCreatureLeft(world)
        elif keys[pygame.K_SPACE] or keys[pygame.K_w]: # and self.consecutive_jumps < 3:
            self.CreatureJump(world)
            self.consecutive_jumps += 1
        elif keys[pygame.K_s]:
            self.CreatureFall(world)
        else:
            x = 0

    # takes in position of mouse click and determines appropriate action (button press etc)
    def handleMouseClick(self, pos, world):
        self.shootBullet(pos, world)

    @staticmethod
    def __overlap(self, l1, r1, l2, r2):
        if l1.xCoord > r2.xCoord or l2.xCoord > r1.xCoord:
            return False
        if l1.yCoord > r2.yCoord or l2.yCoord > r1.yCoord: # swapped because y is inverted
            return False
        return True

    # returns true if desired x,y position intersects with an environment
    def __checkMoveValidity(self, new_topleft, new_botright, world):
        validity = True
        for e in world.environmentList:
            e_top_left = e.top_left
            e_bot_right = e.bot_right
            if Creature.__overlap(None, e_top_left, e_bot_right, new_topleft, new_botright):
                validity = False
        return validity

    # returns a point with the creature's center location (to calculate projectile angles)
    def center(self):
        x_center = self.top_left.xCoord + round((self.bot_right.xCoord - self.top_left.xCoord) / 2)
        y_center = self.top_left.yCoord + round((self.bot_right.yCoord - self.top_left.yCoord) / 2)

        return Point.Point(x_center, y_center)

    # returns a bullet upon mouseclick and adds it to the world list
    def shootBullet(self, pos, world):
        mouse_pos = Point.Point(pos[0], pos[1])
        player_pos = self.center()

        # normalized vector between two points
        direction = mouse_pos.normalized_vector(mouse_pos, player_pos)
        speed = 10
        size = 5
        damage = 10

        bullet = Projectile.Projectile(player_pos, direction, speed, size, damage)
        world.spawn_projectile(bullet)
        return bullet