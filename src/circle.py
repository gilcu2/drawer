
class Circle:
    def __init__(self,x,y,radius,color,label):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.label=label

    def __str__(self):
        return 'Circle(%s,%s,%s,%s,%s)'%(self.x, self.y, self.radius, self.color, self.label)


def circle2dict(obj):
    return obj.__dict__

def dict2circle(dict):
    return Circle(**dict)