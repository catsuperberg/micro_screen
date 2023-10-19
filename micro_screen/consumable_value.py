class ConsumableValue():
    _consumed: bool = False

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        self._consumed = True
        return self._value

    @property
    def consumed(self):
        return self._consumed

    @value.setter
    def value(self, value):
        if self._value == value:
            return
        self._value = value
        self._consumed = False


class ConsumableReader():
    def __init__(self, consumable: ConsumableValue):
        self._consumable = consumable

    @property
    def value(self):
        return self._consumable.value

    @property
    def consumed(self):
        return self._consumable.consumed
