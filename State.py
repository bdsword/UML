from enum import Enum


class UMLComponent(Enum):
    NORMAL = 1
    SELECTED = 2
    DRAGGING = 3

class UMLWorkspace(Enum):
    SELECTING = 1