from DropArea import DropArea
from SelectedBlock import SelectedBlock
from gi.repository import Gdk
import State
from ToolSets import ToolSets



class UMLWorkspace(DropArea):
    def __init__(self):
        super(UMLWorkspace, self).__init__()

        self.state = State.UMLWorkspace.NORMAL
        self.select_start_point = None
        self.select_end_point = None

        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.add_events(Gdk.EventMask.BUTTON_RELEASE_MASK)
        self.add_events(Gdk.EventMask.POINTER_MOTION_MASK)
        self.connect('button-press-event', self.on_button_press)
        self.connect('motion-notify-event', self.on_mouse_motion)
        self.connect('button-release-event', self.on_button_release)
        self.connect('draw', self.on_draw)

    def on_draw(self, widget, cairo_context):
        if self.state == State.UMLWorkspace.SELECTING:
            selected_width = self.select_end_point[0] - self.select_start_point[0]
            selected_height = self.select_end_point[1] - self.select_start_point[1]
            cairo_context.rectangle(self.select_start_point[0], self.select_start_point[1],
                                    selected_width, selected_height)
            cairo_context.set_source_rgba(0.8, 0.1, 0.1, 0.6)
            cairo_context.fill()

    def on_button_press(self, widget, event):
        self.state = State.UMLWorkspace.SELECTING
        self.select_start_point = (event.x, event.y)

    def on_button_release(self, widget, event):
        self.state = State.UMLWorkspace.NORMAL
        self.select_end_point = (event.x, event.y)
        selected_rectangle = ToolSets.make_rectangle(self.select_start_point, self.select_end_point)
        self.foreach(self.update_component_selection, selected_rectangle)
        self.queue_draw()

    def update_component_selection(self, widget, rectangle):
        allocation = widget.get_visible_allocation()
        if ToolSets.rectangle_intersect(allocation, rectangle):
            widget.set_state(State.UMLComponent.SELECTED)
        else:
            widget.set_state(State.UMLComponent.NORMAL)
        widget.queue_draw()

    def on_mouse_motion(self, widget, event):
        if self.state == State.UMLWorkspace.SELECTING:
            self.select_end_point = (event.x, event.y)
            self.queue_draw()

    def on_drag_box_button_press(self, widget, event):
        super(UMLWorkspace, self).on_drag_box_button_press(widget, event)
        return True

    def on_drag_box_button_release(self, widget, event):
        super(UMLWorkspace, self).on_drag_box_button_release(widget, event)
        widget.set_state(State.UMLComponent.SELECTED)
        self.foreach(self.unselect_other_components, widget)
        self.queue_draw()
        return True

    def unselect_other_components(self, unchecked_widget, selected_target):
        if unchecked_widget is not selected_target:
            unchecked_widget.set_state(State.UMLComponent.NORMAL)
            unchecked_widget.queue_draw()
