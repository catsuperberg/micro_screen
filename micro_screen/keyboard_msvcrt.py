import msvcrt
from micro_screen.input_event import InputEventChar, InputEventNavigation, InputEventOperation, Operation, Direction

class KeyboardMsvcrt:
    def __init__(self):
        pass

    def pending_event(self):
        if msvcrt.kbhit():
            char = msvcrt.getch()            
            if char == b'\000':
                return None
            if char == b'\xe0':
                return self._decode_navigation(msvcrt.getch())
            operation = self._decode_operation(char)
            if operation:
                return operation
            return InputEventChar(char.decode())
        
    def _decode_operation(self, operation):        
        if operation == b'\r':
            return InputEventOperation(Operation.ENTER)
        elif operation == b'\x08':
            return InputEventOperation(Operation.CLEAR)
        return None

    def _decode_navigation(self, direction):
        if direction == b'H' or direction == b'K':
            return InputEventNavigation(Direction.PREVIOUS)
        elif direction == b'P' or direction == b'M':
            return InputEventNavigation(Direction.NEXT)