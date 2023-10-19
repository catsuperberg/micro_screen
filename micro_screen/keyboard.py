class Keyboard():
    def pending_event(self) -> any:
        pass

class KeyboardFactory():
    def __init__(self):
        self._modules = [
            {'name': 'micropython', 'callback': self._create_micropython},
            {'name': 'msvcrt', 'callback': self._create_windows},
            {'name': 'termios', 'callback': self._create_termios},
        ]

    def create(self) -> Keyboard:
        for module in self._modules:
            try:
                __import__(module['name'])
                keyboard = module['callback']()
                break
            except ModuleNotFoundError:
                pass
        try: keyboard
        except: raise ModuleNotFoundError("Couldn't find keyboard class that would work on this platform")
        return keyboard

    def _create_termios(self):
        from micro_screen.keyboard_termios import KeyboardTermios
        return KeyboardTermios()

    def _create_windows(self):
        from micro_screen.keyboard_msvcrt import KeyboardMsvcrt
        return KeyboardMsvcrt()

    def _create_micropython(self):
        from micro_screen.keyboard_micropython import KeyboardMicropython
        return KeyboardMicropython()