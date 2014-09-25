from gi.repository import Gdk
from DragBox import DragBox
import State


class UMLComponent(DragBox):
    def __init__(self):
        super(UMLComponent, self).__init__()
        self.connect('draw', self.on_draw)
        self.set_app_paintable(True)
        self.selected_block_size = 10
        self.show_selected_line = True
        self.selected_line_width = 3
        self.selected_line_dashes = [6.0]

    def show_selected_line(self, setting):
        self.show_selected_line = setting

    def set_selected_line_width(self, line_width):
        self.selected_line_width = line_width

    def set_selected_line_dashes(self, line_dashes):
        self.selected_line_dashes = line_dashes

    def set_selected_block_size(self, selected_block_size):
        self.selected_block_size = selected_block_size

    def on_draw(self, widget, cairo_context):
        print(widget.state)
        self.draw_background(cairo_context)
        if self.state == State.SELECTED:
            if self.show_selected_line == True:
                self.draw_selected_line(cairo_context)
            self.draw_selected_block(cairo_context)

    def draw_selected_block(self, cairo_context):
        allocation = self.get_allocation()
        b_size = self.selected_block_size
        draw_axis_x = allocation.width/2
        draw_axis_y = allocation.height/2
        cairo_context.rectangle(draw_axis_x-b_size/2, 0, b_size, b_size)
        cairo_context.rectangle(draw_axis_x-b_size/2, allocation.height-b_size, b_size, b_size)
        cairo_context.rectangle(0, draw_axis_y-b_size/2, b_size, b_size)
        cairo_context.rectangle(allocation.width-b_size, draw_axis_y-b_size/2, b_size, b_size)
        cairo_context.set_source_rgb(1, 0, 0)
        cairo_context.fill()

    def draw_selected_line(self, cairo_context):
        allocation = self.get_allocation()
        cairo_context.rectangle(self.selected_block_size/2, self.selected_block_size/2,
                                allocation.width-self.selected_block_size,
                                allocation.height-self.selected_block_size)
        cairo_context.set_source_rgb(1, 0, 0)
        cairo_context.set_dash(self.selected_line_dashes, 0)
        cairo_context.set_line_width(self.selected_line_width)
        cairo_context.stroke()

    def draw_background(self, cairo_context):
        allocation = self.get_allocation()
        cairo_context.rectangle(self.selected_block_size/2, self.selected_block_size/2,
                                allocation.width-self.selected_block_size,
                                allocation.height-self.selected_block_size)
        cairo_context.set_source_rgb(0, 1, 0)
        cairo_context.fill()