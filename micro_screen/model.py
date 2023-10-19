from micro_screen.input_state import InputState
from micro_screen.coroutine_provider import CoroutineProvider
from micro_screen.keyboard import Keyboard
from micro_screen.screen_state import ScreenState

class Model():
    input_state: InputState
    
    def __init__(self, coroutine_provider: CoroutineProvider, keyboard: Keyboard, screen_state: ScreenState):
        self._coroutine_provider = coroutine_provider
        self._keyboard = keyboard
        self._screen_state = screen_state