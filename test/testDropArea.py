from DragBox import DragBox
from DropArea import DropArea
from gi.repository import Gtk
from gi.repository import Gdk


class TestWindow(Gtk.Window):
    def __init__(self):
        super(TestWindow, self).__init__(title="TestWindow")
        self.drop_area = DropArea()
        self.drop_area.set_size(450, 450)
        self.drop_area.set_size_request(450, 450)
        self.drop_area.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0.3, 0.5, 1))

        self.fixed = Gtk.Fixed()
        self.fixed.put(self.drop_area, 100, 100)
        self.add(self.fixed)

        drag_box = DragBox()
        drag_box.set_size_request(200, 200)
        drag_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1, 0, 0.5))
        self.drop_area.add_drag_box(drag_box, 100, 20)

test_window = TestWindow()
test_window.set_size_request(640, 640)
test_window.connect('delete-event', Gtk.main_quit)
test_window.show_all()
Gtk.main()