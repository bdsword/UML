from DragBox import DragBox
from Line import Line


class UMLRelation(Line, DragBox):
    def __init__(self):
        super(UMLRelation, self).__init__()
        # TODO: make sure if I would like to make draw with gtk original draw-signal
        # self.connect('draw', self.on_draw)

    # def on_draw(self, widget, cairo_context):
    #     print('on draw')

    def draw(self, cairo_context):
        #  This is a basic UML relation line draw implementation,
        #  you can override it to make your own one.
        cairo_context.set_source_rgb(1, 1, 1)
        cairo_context.set_line_width(10)
        if len(self.points) != 0:
            begin_point = self.points[0]
            begin_point_coord = begin_point.get_coordinate()
            cairo_context.move_to(begin_point_coord[0], begin_point_coord[1])
            for point in self.points:
                point_coord = point.get_coordinate()
                cairo_context.line_to(point_coord[0], point_coord[1])
            cairo_context.stroke()

    def append_component(self, component):
        component.register('on_draw', self.on_component_draw)
        self.points.append(component)

    def on_component_draw(self, data):
        component = data['widget']
        allocation = component.get_visible_allocation()