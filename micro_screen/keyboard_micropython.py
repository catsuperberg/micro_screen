import sys, select
from micro_screen.keypress_decoder_terminal import KeypressDecoderTerminal
from micro_screen.keyboard import Keyboard

class KeyboardMicropython(Keyboard):    
    MP_STREAM_POLL_RD = 1
    
    def __init__(self):
        self._decoder = KeypressDecoderTerminal()
        self._poll = select.poll()
        self._poll.register(sys.stdin)

    def pending_event(self):
        _, flags = self._poll.poll(0)[0]
        if flags & self.MP_STREAM_POLL_RD:
            return self._decoder.decode(sys.stdin.read(1).encode('ascii'))
        # else:
        #     return None