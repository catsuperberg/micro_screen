import sys
from micro_screen.input_event import InputEventChar, InputEventNavigation, InputEventOperation, Operation, Direction

class KeypressDecoderTerminal():
    def __init__(self):
        pass

    def decode(self, key_event):
        if key_event:
            operation = self._decode_operation(key_event)
            if(operation is not None):
                return operation
            navigation = self._decode_navigation(key_event)
            if(navigation is not None):
                return navigation
            return InputEventChar(key_event.decode('ascii'))
        # else:
        #     return None

    def _decode_operation(self, char):
        if char == b'\n':
            return InputEventOperation(Operation.ENTER)
        elif char == b'\x7f' or char == b'\x08':
            return InputEventOperation(Operation.CLEAR)
        return None

    def _decode_navigation(self, char):
        if char != b'\x1b':
            return None
        direction = char + sys.stdin.read(2).encode('ascii')
        if direction == b'\x1b[A' or direction == b'\x1b[D':
            return InputEventNavigation(Direction.PREVIOUS)
        elif direction == b'\x1b[B' or direction == b'\x1b[C':
            return InputEventNavigation(Direction.NEXT)