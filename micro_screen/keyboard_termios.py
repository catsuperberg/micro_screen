import termios, fcntl, sys, os
from micro_screen.keypress_decoder_terminal import KeypressDecoderTerminal
from micro_screen.keyboard import Keyboard

class KeyboardTermios(Keyboard):
    def __init__(self):
        self._decoder = KeypressDecoderTerminal()
        
        fd = sys.stdin.fileno()
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    def pending_event(self):
        return self._decoder.decode(sys.stdin.read(1).encode('ascii'))