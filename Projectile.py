class Projectile:
    speed = None # speed of projectile in pixels/s
    size = None # radius of bullet in pixels
    x_vel = None # speed of projectile in x direction
    y_vel = None # speed of projectile in y direction
    x_pos = None
    y_pos = None

    def __init__(self, position, direction, speed, size):
        self.x_pos = position.xCoord
        self.y_pos = position.yCoord
        self.speed = speed
        self.direction = direction
        self.size = size

        self.x_vel = round(direction[0]) * round(speed)
        self.y_vel = round(direction[1]) * round(speed)

    def update_position(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel