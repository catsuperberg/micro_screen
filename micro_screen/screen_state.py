from .consumable_value import ConsumableReader
from micro_screen.line import Line
from micro_screen.displayable import Displayable, InputAttributes, OutputAttributes

class Field():
    _coordinates: tuple[int, int]
    _size: int
    
    @property
    def coordinates(self):
        return self._coordinates
    
    @property
    def size(self):
        return self._size
    
    def __init__(self, coordinates: tuple[int, int], size: int):
        self._coordinates = coordinates
        self._size = size
    
class DynamicField(Field):
    _consumable: ConsumableReader
    
    def __init__(self, coordinates: tuple[int, int], size: int, consumable: ConsumableReader):
        super().__init__(coordinates, size)
        self._consumable = consumable
        
    @property
    def consumable(self):
        return self._consumable
    
    def __eq__(self, other):
        if not isinstance(other, DynamicField):
            return False
        
        return self._consumable == other.consumable and \
               self._coordinates == other.coordinates and \
               self._size == other.size

class InputField(Field):    
    def __init__(self, coordinates: tuple[int, int], size: int, on_apply):
        super().__init__(coordinates, size)
        self._on_apply = on_apply
        
    @property
    def on_apply(self):
        return self._on_apply
    
    def __eq__(self, other):
        if not isinstance(other, InputField):
            return False
        
        return self._on_apply == other.on_apply and\
               self._coordinates == other.coordinates and \
               self._size == other.size

class ScreenState():
    _static_lines: list[str] = []
    _dynamic_fields: list[DynamicField] = []
    _inputs: list[InputField] = []
    
    selected_input: int = 0
    input_string: str = ''
    
    def __init__(self, lines: list[Line]):    
        row = 0
        for displaybles in lines:
            column = 0
            static_line_elements = []
            for displayable in displaybles:
                if isinstance(displayable, str):
                    static_line_elements.append(displayable)
                    column += len(displayable)
                elif isinstance(displayable, Displayable):
                    static_line_elements.append(' ' * displayable.size)
                    self.parse_displayable(row, column, displayable)
                    column += displayable.size
            self._static_lines.append(''.join(static_line_elements))
            row += 1

    def parse_displayable(self, row, column, displayable):
        if isinstance(displayable, InputAttributes):
            self._inputs.append(InputField([row, column], displayable.size, displayable.on_apply))
        elif isinstance(displayable, OutputAttributes):
            self._dynamic_fields.append(DynamicField([row, column], displayable.size, displayable.data))
    
class ScreenStateReader():
    def __init__(self, state: ScreenState):
        self._state = state
        
    @property
    def static_lines(self):
        return self._state._static_lines
    
    @property
    def dynamic_fields(self):
        return self._state._dynamic_fields
    
    @property
    def inputs(self):
        return self._state._inputs
    
    @property
    def selected_input(self):
        return self._state.selected_input
    
    @property
    def input_string(self):
        return self._state.input_string
    