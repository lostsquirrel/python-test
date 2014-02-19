class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else :
            return False
            
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        super(self,angle,angle,angle)

def test(x):
    for x in range(1,10):
        print x