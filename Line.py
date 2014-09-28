

class Line:
    def __init__(self):
        self.points = []

    def append_point(self, point):
        self.points.append(point)

    def insert_point(self, index, point):
        self.points.insert(index, point)

    def remove_point(self, point):
        self.points.remove(point)