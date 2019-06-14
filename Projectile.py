import Point, math


class Projectile:
    speed = None # speed of projectile in pixels/s
    size = None # radius of bullet in pixels
    x_vel = None # speed of projectile in x direction
    y_vel = None # speed of projectile in y direction
    x_pos = None
    y_pos = None
    damage = None

    #properties for hitbox
    top_left = None
    bot_right = None

    def __init__(self, position, direction, speed, size, damage):
        self.x_pos = position.xCoord
        self.y_pos = position.yCoord
        self.speed = speed
        self.direction = direction
        self.size = size
        self.damage = damage

        self.x_vel = direction[0] * speed
        self.y_vel = direction[1] * speed

    def update_position(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

        self.top_left = Point.Point(self.x_pos - self.size, self.y_pos - self.size)
        self.bot_right = Point.Point(self.x_pos + self.size, self.y_pos + self.size)

    # returns entity if bullet is within 1 pixel of it **registers as hit**
    def apply_damage(self, world):
        collisions = []
        enemies = world.enemy_list
        for en in enemies:
            if self.__overlap(None, self.top_left, self.bot_right, en.top_left, en.bot_right):
                collisions.append([self, en])
                if self in world.projectileList:
                    world.projectileList.remove(self) # remove bullet once it hits an enemy
                en.health -= self.damage
                en.green = min(en.green + 20, 255)
                en.color = [255, en.green, 0]

    #bullets disappear when they come in contact with an environment
    def absorb_projectile(self, world):
        environments = world.environmentList
        for e in environments:
            if self.__overlap(None, self.top_left, self.bot_right, e.top_left, e.bot_right):
                if self in world.projectileList:
                    world.projectileList.remove(self)
            
    @staticmethod
    def __overlap(self, l1, r1, l2, r2):
        if l1.xCoord > r2.xCoord or l2.xCoord > r1.xCoord:
            return False
        if l1.yCoord > r2.yCoord or l2.yCoord > r1.yCoord: # swapped because y is inverted
            return False
        return True
