import sys
import re
from micro_screen.screen_state import ScreenStateReader

class Presenter():
    def __init__(self, state_reader: ScreenStateReader):
        self._state_reader = state_reader
        
    def update_screen(self):
        pass
    
    def _full_redraw(self):
        pass
    
    def _redraw_updated(self):
        pass
    
    def _draw_static(self):
        pass
    
    def _draw_unconsumed_dynamics(self):
        pass
    
    def _draw_input_on_change(self):
        pass
    
    def _clear_previous_input(self):
        pass
    
    def _detect_redraw_needed(self):
        pass
        
    def _clear_screen(self):
        sys.stdout.write('\x1b[2J')
        sys.stdout.write('\x1b[H')
        
    def _move_cursor(self, row, column):
        sys.stdout.write("\x1b[{};{}H".format(row, column))
    
    def _hide_cursor(self):
        sys.stdout.write('\033[?25l')    
         
    def _show_cursor(self):
        sys.stdout.write('\033[?25h')  
        
    def _get_cursor(self):
        sys.stdout.write("\x1b[6n")
        answer = ""
        while not (answer := answer + sys.stdin.read(1)).endswith('R'): pass
        rx = re.compile(r".*\[(\d*);(\d*)R")
        res = rx.match(answer)
        return res.group(1), res.group(2)