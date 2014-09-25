from gi.repository import Gdk
from gi.repository import Gtk
from DragBox import DragBox
import State


class UMLComponent(DragBox):
    def __init__(self):
        super(UMLComponent, self).__init__()
        # init class field
        self.selected_block_size = 10
        self.show_selected_line = True
        self.selected_line_width = 3
        self.selected_line_dashes = [6.0]

        self.connect('draw', self.on_draw)
        self.set_app_paintable(True)
        self.layout = Gtk.Layout()  # use this layout manage inside widget
        self.add(self.layout)

        self.selected_blocks = self.setup_selected_block()

    def setup_selected_block(self):
        selected_blocks = []
        for i in range(4):
            selected_blocks.append(SelectedBlock())
            selected_blocks[i].set_size_request(self.selected_block_size, self.selected_block_size)
            self.layout.add(selected_blocks[i])
        return selected_blocks

    def rearrange_widgets(self):
        # #############
        #     0      #
        #            #
        #3          1#
        #            #
        #     2      #
        ##############
        allocation = self.get_allocation()
        b_size = self.selected_block_size
        draw_axis_x = allocation.width / 2
        draw_axis_y = allocation.height / 2
        position = [[draw_axis_x - b_size / 2, 0],
                    [draw_axis_x - b_size / 2, allocation.height - b_size],
                    [0, draw_axis_y - b_size / 2],
                    [allocation.width - b_size, draw_axis_y - b_size / 2]]
        for i in range(4):
            self.layout.move(self.selected_blocks[i], position[i][0], position[i][1])

    def show_selected_line(self, setting):
        self.show_selected_line = setting

    def set_selected_line_width(self, line_width):
        self.selected_line_width = line_width

    def set_selected_line_dashes(self, line_dashes):
        self.selected_line_dashes = line_dashes

    def set_selected_block_size(self, selected_block_size):
        self.selected_block_size = selected_block_size

    def on_draw(self, widget, cairo_context):
        self.rearrange_widgets()
        self.draw_background(cairo_context)

        if self.state == State.SELECTED:
            if self.show_selected_line:
                self.draw_selected_line(cairo_context)
            for selected_block in self.selected_blocks:
                selected_block.show()
            # self.draw_selected_block(cairo_context)
        else:
            for selected_block in self.selected_blocks:
                selected_block.hide()
                # pass

    def draw_selected_block(self, cairo_context):
        allocation = self.get_allocation()
        b_size = self.selected_block_size
        draw_axis_x = allocation.width / 2
        draw_axis_y = allocation.height / 2
        cairo_context.rectangle(draw_axis_x - b_size / 2, 0, b_size, b_size)
        cairo_context.rectangle(draw_axis_x - b_size / 2, allocation.height - b_size, b_size, b_size)
        cairo_context.rectangle(0, draw_axis_y - b_size / 2, b_size, b_size)
        cairo_context.rectangle(allocation.width - b_size, draw_axis_y - b_size / 2, b_size, b_size)
        cairo_context.set_source_rgb(1, 0, 0)
        cairo_context.fill()

    def draw_selected_line(self, cairo_context):
        allocation = self.get_allocation()
        cairo_context.rectangle(self.selected_block_size / 2, self.selected_block_size / 2,
                                allocation.width - self.selected_block_size,
                                allocation.height - self.selected_block_size)
        cairo_context.set_source_rgb(1, 0, 0)
        cairo_context.set_dash(self.selected_line_dashes, 0)
        cairo_context.set_line_width(self.selected_line_width)
        cairo_context.stroke()

    def draw_background(self, cairo_context):
        allocation = self.get_allocation()
        cairo_context.rectangle(self.selected_block_size / 2, self.selected_block_size / 2,
                                allocation.width - self.selected_block_size,
                                allocation.height - self.selected_block_size)
        cairo_context.set_source_rgb(0, 1, 0)
        cairo_context.fill()