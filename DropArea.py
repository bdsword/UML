from gi.repository import Gtk
from Point import Point
import State
import cairo


class DropArea(Gtk.Layout):
    def __init__(self):
        super(DropArea, self).__init__()
        self.press_point = None  # in drag-box's coordinate space

    def add_drag_box(self, drag_box, x, y):
        self.put(drag_box, x, y)
        drag_box.connect('button-press-event', self.on_drag_box_button_press)
        drag_box.connect('button_release_event',
                         self.on_drag_box_button_release)
        drag_box.connect('motion-notify-event', self.on_drag_box_mouse_motion)

    def on_drag_box_button_press(self, widget, event):
        self.press_point = Point(event.x, event.y)

    def on_drag_box_button_release(self, widget, event):
        pass

    def on_drag_box_mouse_motion(self, widget, event):
        (x, y) = self.get_absolute_coord(widget, event.x, event.y)
        self.move(widget, x-self.press_point.x, y-self.press_point.y)

    def get_absolute_coord(self, widget, x, y):
        allocation = widget.get_allocation()
        return x+allocation.x, y+allocation.y

    ##########################################################
    #    This method is deprecated unless you want to        #
    #    forbidden widget from moving out of the container   #
    ##########################################################
    def out_range_adjust(self, widget, x, y):
        allocation = widget.get_allocation()
        self_allocation = self.get_allocation()
        if x < 0:
            x = 0
        elif x+allocation.width > self_allocation.width:
            x = self_allocation.width - allocation.width
        if y < 0:
            y = 0
        elif y+allocation.height > self_allocation.height:
            y = self_allocation.height - allocation.height
        return x, y
