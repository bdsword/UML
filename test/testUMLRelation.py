from UMLWorkspace import UMLWorkspace
from UserCaseComponent import UserCaseComponent
from gi.repository import Gtk
from gi.repository import Gdk
from UMLRelation import UMLRelation


class TestWindow(Gtk.Window):
    def __init__(self):
        super(TestWindow, self).__init__(title="TestUMLRelation")
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

        drag_box2 = UserCaseComponent(50, 80)
        drag_box2.set_selected_block_size(4)
        drag_box2.set_selected_line_width(4)
        drag_box2.set_selected_line_visible(True)
        self.drop_area.add_drag_box(drag_box2, 200, 200)

        drag_line = UMLRelation()
        drag_line.append_component(drag_box)
        drag_line.append_component(drag_box2)
        self.drop_area.add_relation_line(drag_line)


test_window = TestWindow()
test_window.set_size_request(640, 640)
test_window.connect('delete-event', Gtk.main_quit)
test_window.show_all()
Gtk.main()