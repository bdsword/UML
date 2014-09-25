from gi.repository import Gtk
import State


class DragBox(Gtk.EventBox):
    """
        A EventBox based class which is supported
    dragging and dropping in a drop-area.
    """
    def __init__(self):
        super(DragBox, self).__init__()
        self.state = State.NORMAL

    def set_state(self, state):
        self.state = state
