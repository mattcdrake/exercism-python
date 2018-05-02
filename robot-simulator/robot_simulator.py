# Globals for the bearings
# Change the values as you see fit
EAST = "E"
NORTH = "N"
WEST = "W"
SOUTH = "S"

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        pass
    
    @property
    def coordinates(self):
        return (self.x, self.y)

    def simulate(self, direction):
        for instruction in direction:
            if instruction == "L":
                self.turn_left()
            elif instruction == "R":
                self.turn_right()
            elif instruction == "A":
                self.advance()
    
    def turn_left(self):
        if self.bearing == EAST:
            self.bearing = NORTH
        elif self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
    
    def turn_right(self):
        if self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH
        elif self.bearing == NORTH:
            self.bearing = EAST
    
    def advance(self):
        if self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == WEST:
            self.x -= 1
        elif self.bearing == NORTH:
            self.y += 1

