from UMLWorkspace import UMLWorkspace
from UserCaseComponent import UserCaseComponent
from gi.repository import Gtk
from gi.repository import Gdk


class TestWindow(Gtk.Window):
    def __init__(self):
        super(TestWindow, self).__init__(title="TestUserCaseComponent")
        self.drop_area = UMLWorkspace()
        self.drop_area.set_size(450, 450)
        self.drop_area.set_size_request(450, 450)
        self.drop_area.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0.3, 0.5, 1))

        self.fixed = Gtk.Fixed()
        self.fixed.put(self.drop_area, 100, 100)
        self.add(self.fixed)
        
        drag_box = UserCaseComponent(100, 100)
        drag_box.set_selected_block_size(8)
        drag_box.set_size(300, 120)
        drag_box.set_selected_line_width(4)
        drag_box.set_selected_line_visible(True)
        drag_box.set_selected_line_dashes([0.3, 0.5, 1, 0.2, 0.8])
        self.drop_area.add_drag_box(drag_box, 100, 20)

test_window = TestWindow()
test_window.set_size_request(640, 640)
test_window.connect('delete-event', Gtk.main_quit)
test_window.show_all()
Gtk.main()