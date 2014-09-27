from DropArea import DropArea
from SelectedBlock import SelectedBlock
import State


class UMLWorkspace(DropArea):
    def __init__(self):
        super(UMLWorkspace, self).__init__()

    def on_drag_box_button_release(self, widget, event):
        widget.set_state(State.SELECTED)
        self.queue_draw()