from gi.repository import Gtk


class DragBox(Gtk.EventBox):
    """
        A EventBox based class which is supported
    dragging and dropping in a drop-area.
    """
    def __init__(self):
        super(DragBox, self).__init__()
