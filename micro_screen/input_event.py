class Operation():
    CLEAR = 1
    ENTER = 2
    
class Direction():
    NEXT = 1
    PREVIOUS = -1


class InputEventChar():
    def __init__(self, char: str):
        self._char = char
        
    @property
    def char(self) -> str:
        return self._char
        
    def __str__(self) -> str:
        return f"InputEventChar({self.char})"

class InputEventOperation():
    def __init__(self, operation_type: Operation):
        self._operation_type = operation_type
                
    @property
    def operation_type(self) -> Operation:
        return self._operation_type
    
    def __str__(self) -> str:
        return f"InputEventOperation({self.operation_type})"
        

class InputEventNavigation():
    def __init__(self, direction: Direction):
        self._direction = direction
        
    @property
    def direction(self) -> Operation:
        return self._direction
    
    def __str__(self) -> str:
        return f"InputEventNavigation({self.direction})"