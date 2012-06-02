import numpy as np

class point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

class line():
    def __init__(self, p1, p2):
        #~ self.points = [p1, p2]
        if p2.x == p1.x:
            raise ValueError, "x1 must be different of x2"
        self.m = (p2.y - p1.y)/(p2.x - p1.x)
        self.n = p2.y - p2.x * self.m
        self.minx = np.min([p1.x, p2.x])
        self.miny = np.min([p1.y, p2.y])
        self.maxx = np.max([p1.x, p2.x])
        self.maxy = np.max([p1.y, p2.y]) 

    def __repr__(self):
        return "y = %s * x + %s"% (self.m, self.m)

    def __str__(self):
        return "y = %s * x + %s"% (self.m, self.m)

    def isxin(self, x):
        return self.minx <= x <= self.maxx

    def isyin(self, y):
        return self.miny <= y <= self.maxy

    def y(self, x):
        if self.isxin(x):
            return self.m * x + self.n
        else:
            return None

    def x(self, y):
        if self.isyin(y):
            return  (y - self.n) / self.m
        else:
            return None

    def area(self, x1=None, x2=None):
        if x1 == None:
            x1 = self.minx
        if x2 == None:
            x2 = self.maxx 
        if self.isxin(x1) and self.isxin(x2):
            return (self.y(x1) + self.y(x1)) * (x2 - x1)/2.0
        else:
            raise ValueError, "x values out of range"


class polyline():
    def __init__(self, lines=None):
        if lines == None:
            self.lines = []
        else:
            self.lines = lines

    def addline(self,ln):
        # addline at last
        self.lines.append(ln)


def main():
    print 'ok'
    a = point(0, 1)
    b = point(2, 3)
    d = point(3, 5)
    g = point(10, 2)
    print a.x , a.y
    c = line(a, b)
    print c
    e = line(b, d)
    h = line(d, g)
    yv = e.y(2.5)
    print yv
    print e.x(yv)
    f = polyline([c, e])
    print f.lines
    print c.isxin(5)
    f.addline(h)
    print f.lines
    print e.area(2.2, 3)
    print c.area()

if __name__ == '__main__':
    main()

