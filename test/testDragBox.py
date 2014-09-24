import dragBox
from gi.repository import Gtk


class TestWindow(Gtk.Window):
    def __init__(self):
        super(TestWindow, self).__init__(title="TestWindow")
        self.drag_box = dragBox.DragBox()
        self.add(self.drag_box)

test_window = TestWindow()
test_window.set_size_request(640, 480)
test_window.connect('delete-event', Gtk.main_quit)
test_window.show_all()
Gtk.main()
