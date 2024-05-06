import math

class Projectile():
    def __init__(self, x, y, dx, dy, spd, angle):
        self.x = x
        self.y = y
        self.dir = [dx,dy]
        self.spd = spd
        self.velocity = [
            self.spd * math.cos(angle),
            self.spd * math.sin(angle)
        ]
        
class Enemy():
    def __init__(self, x, y, spd):
        self.x = x
        self.y = y
        self.spd = spd
        
def dist(ax, ay, bx, by):
    return math.sqrt((ax-bx)**2+(ay-by)**2)

projectileList = []
enemyList = []