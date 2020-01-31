import Point, random


class Enemy:
    gravity = 3
    green = 120
    color = None
    speed = None #pixels per second
    top_left = None
    bot_right = None
    x_size = None
    y_size = None
    health = None

    # properties for obstacle detection
    stuck = None # whether enemy is stuck behind wall
    stuck_direction = None # which direction enemy is prevented from moving in
    last_move = None # 1 for up, 2 for right, 3 for down, 4 for left
    last_position = None

    def __init__(self, top_left, bot_right, speed, health):
        self.speed = speed
        self.top_left = top_left
        self.bot_right = bot_right
        self.health = health

        self.x_size = bot_right.xCoord - top_left.xCoord
        self.y_size = bot_right.yCoord - top_left.yCoord
        self.color = (255, self.green, 0)

        self.stuck = False

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

    def move_towards_player(self, world):
        player = world.creatureList[0]
        # 4 cases for player location relative to player
        p_pos = player.center()
        self_pos = self.center()

        self.last_position = self.top_left
        obs = self.check_for_obstacles() # returns direction of obstacle if any, otherwise returns 0
        print(obs)

        decision = random.randint(1, 2)
        # player is above and to the right, so move up or right
        if p_pos.xCoord > self_pos.xCoord and p_pos.yCoord < self_pos.yCoord:
            if decision == 1:
                self.CreatureJump(world)
            elif decision == 2:
                self.moveCreatureRight(world)
        # player is above and to the left
        elif p_pos.xCoord < self_pos.xCoord and p_pos.yCoord < self_pos.yCoord:
            if decision == 1:
                self.CreatureJump(world)
            elif decision == 2:
                self.moveCreatureLeft(world)
        # player is below and to the left
        elif p_pos.xCoord < self_pos.xCoord and p_pos.yCoord > self_pos.yCoord:
            if decision == 1:
                self.CreatureFall(world)
            elif decision == 2:
                self.moveCreatureLeft(world)
        # player is below and to the right
        elif p_pos.xCoord > self_pos.xCoord and p_pos.yCoord > self_pos.yCoord:
            if decision == 1:
                self.CreatureFall(world)
            elif decision == 2:
                self.moveCreatureRight(world)

    # returns direction if stuck behind obstacle (1 for up, 2 for right, 3 for down, 4 for side)
    def check_for_obstacles(self):
        # check top and right directions if self.last_move = 1
        if self.last_move == 1:
            if self.top_left.yCoord == self.last_position.yCoord:
                return 1
        if self.last_move == 2:
            if self.top_left.xCoord == self.last_position.xCoord:
                return 2
        if self.last_move == 3:
            if self.top_left.yCoord == self.last_position.yCoord:
                return 3
        if self.last_move == 4:
            if self.top_left.yCoord == self.last_position.yCoord:
                return 4
        return 0

        #shared with creature class:
    def moveCreatureRight(self, world):
        new_topleft = Point.Point(self.top_left.xCoord + self.speed, self.top_left.yCoord)
        new_botright = Point.Point(self.bot_right.xCoord + self.speed, self.bot_right.yCoord)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright
        self.last_move = 2

    def moveCreatureLeft(self, world):
        new_topleft = Point.Point(self.top_left.xCoord - self.speed, self.top_left.yCoord)
        new_botright = Point.Point(self.bot_right.xCoord - self.speed, self.bot_right.yCoord)
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright
        self.last_move = 4

    def applyGravity(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord + Enemy.gravity)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord + Enemy.gravity)
        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright

    def CreatureJump(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord - self.speed)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord - self.speed)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright
        self.last_move = 1

    def CreatureFall(self, world):
        new_topleft = Point.Point(self.top_left.xCoord, self.top_left.yCoord + self.speed)
        new_botright = Point.Point(self.bot_right.xCoord, self.bot_right.yCoord + self.speed)

        if self.__checkMoveValidity(new_topleft, new_botright, world):
            self.top_left = new_topleft
            self.bot_right = new_botright
        self.last_move = 3

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
