from micro_screen.consumable_value import ConsumableReader

class Displayable():
    _size: int
    
    def __init__(self, size: int):
        self._size = size
    
    @property
    def size(self):
        return self._size
    
class InputAttributes(Displayable):    
    def __init__(self, size: int, on_apply):
        super().__init__(size)
        self._on_apply = on_apply 
    
    @property
    def on_apply(self):
        return self._on_apply
    
class OutputAttributes(Displayable):
    def __init__(self, size: int, data: ConsumableReader):
        if not isinstance(data, ConsumableReader):
            raise TypeError("Only ConsumableReader allowed as data")   
        super().__init__(size)      
        self._data = data
    
    @property
    def data(self):
        return self._data