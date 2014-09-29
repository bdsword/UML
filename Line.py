from Point import Point


class Line:
    def __init__(self):
        super(Line, self).__init__()
        self.points = []

    def append_point(self, point):
        assert(isinstance(point, Point))
        self.points.append(point)

    def insert_point(self, index, point):
        assert(isinstance(point, Point))
        self.points.insert(index, point)

    def remove_point(self, point):
        assert(isinstance(point, Point))
        self.points.remove(point)