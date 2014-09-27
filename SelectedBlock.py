from gi.repository import Gtk


class SelectedBlock(Gtk.EventBox):
    def __init__(self):
        super(SelectedBlock, self).__init__()
        self.set_app_paintable(True)
        self.connect('draw', self.on_draw)

    def on_draw(self, widget, cairo_context):
        allocation = self.get_allocation()
        cairo_context.rectangle(0, 0, allocation.width, allocation.height)
        cairo_context.set_source_rgb(1, 1, 1)
        cairo_context.fill()