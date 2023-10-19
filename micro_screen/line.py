from micro_screen.displayable import Displayable

class Line(list):
    def __init__(self, iterable: list[str | Displayable]):
        super().__init__(item for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        super().append(item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(item for item in other)