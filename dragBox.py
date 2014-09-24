from gi.repository import Gtk


class DragBox(Gtk.EventBox):
    def __init__(self):
        super(DragBox, self).__init__()

    def get_state(self):
        return self.state