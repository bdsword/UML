import cairo


class ToolSets:
    @staticmethod
    def rectangle_intersect(rect1, rect2):
        return not (rect2.x > rect1.x + rect1.width or
                    rect2.x + rect2.width < rect1.x or
                    rect2.y > rect1.y + rect1.height or
                    rect2.y + rect2.height < rect1.y)

    @staticmethod
    def make_rectangle(start_point, end_point):
        (start_point, end_point) = sorted([start_point, end_point], key=lambda point: point[0])  # sort by x-coordinate
        width = abs(end_point[0] - start_point[0])
        height = abs(end_point[1] - start_point[1])
        if start_point[1] < end_point[1]:
            y = start_point[1]
        else:
            y = end_point[1]
        return cairo.RectangleInt(int(start_point[0]), int(y), int(width), int(height))