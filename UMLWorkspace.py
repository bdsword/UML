from DropArea import DropArea
from SelectedBlock import SelectedBlock
from gi.repository import Gdk
import State



class UMLWorkspace(DropArea):
    def __init__(self):
        super(UMLWorkspace, self).__init__()

        self.state = State.UMLWorkspace.SELECTING

        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.add_events(Gdk.EventMask.BUTTON_RELEASE_MASK)
        self.add_events(Gdk.EventMask.POINTER_MOTION_MASK)
        self.connect('button-press-event', self.on_button_press)
        self.connect('motion-notify-event', self.on_mouse_motion)
        self.connect('button-release-event', self.on_button_release)

    def on_button_press(self, widget, event):
        print('on button press')

    def on_button_release(self, widget, event):
        print('on button release')

    def on_mouse_motion(self, widget, event):
        print('on mouse motion')

    def on_drag_box_button_release(self, widget, event):
        widget.set_state(State.UMLComponent.SELECTED)
        self.queue_draw()

    def on_drag_box_button_press(self, widget, event):
        print('drag-box press')