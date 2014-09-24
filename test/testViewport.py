from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib
from dragBox import DragBox
from dropArea import DropArea

class TestWindow(Gtk.Window):
    def __init__(self):
        super(TestWindow, self).__init__(title="Test Viewport")
        self.view_port = Gtk.Viewport()
        self.add(self.view_port)

        drop_area = DropArea(640, 480)
        drag_box = DragBox()
        drag_box.set_size_request(50, 50)
        drag_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1, 1, 0.3))
        drop_area.add_drag_box(drag_box, 300, 310)
        self.view_port.add(drop_area)


test_window = TestWindow()
test_window.show_all()
test_window.set_size_request(400, 400)

GLib.timeout_add(3000, lambda : print(test_window.view_port.get_allocation().width, test_window.view_port.get_allocation().height))

test_window.connect('delete-event', Gtk.main_quit)
Gtk.main()