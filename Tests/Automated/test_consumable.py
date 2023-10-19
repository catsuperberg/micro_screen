import unittest
from micro_screen.consumable_value import ConsumableValue, ConsumableReader

class TestConsumable(unittest.TestCase):
    initial_value = 'initial value'
    modified_value = 'modified value'

    class Container():
        data: ConsumableReader

        def __init__(self, consumable: ConsumableReader | ConsumableValue):
            if isinstance(self, ConsumableReader):
                self.data = consumable
            else:
                self.data = ConsumableReader(consumable)

        def check_consumed(self):
            return self.data.consumed

        def read_value(self):
            return self.data.value

        def attempt_write(self, value):
            try:
                self.data.value = value
            except:
                pass

    def test_value_change_as_variable(self):   
        consumable = ConsumableValue(self.initial_value)
        consumable.value = self.modified_value
        self.assertEqual(consumable.value, self.modified_value)

    def test_value_is_consumed(self):
        consumable = ConsumableValue(self.initial_value)
        self.assertFalse(consumable.consumed)
        _ = consumable.value
        self.assertTrue(consumable.consumed)

    def test_value_updated_in_class(self):
        consumable = ConsumableValue(self.initial_value)
        container = self.Container(consumable)
        consumable.value = self.modified_value
        self.assertEqual(container.read_value(), self.modified_value)

    def test_consumed_from_class(self):
        consumable = ConsumableValue(self.initial_value)
        container = self.Container(consumable)
        self.assertFalse(consumable.consumed)
        self.assertEqual(container.check_consumed(), consumable.consumed)
        container.read_value()
        self.assertTrue(consumable.consumed)
        self.assertEqual(container.check_consumed(), consumable.consumed)

    def test_reader_does_not_write(self):
        consumable = ConsumableValue(self.initial_value)
        container = self.Container(consumable)
        container.attempt_write(self.modified_value)
        self.assertEqual(consumable.value, self.initial_value)

    def test_does_not_change_consumed_on_same_value(self):
        consumable = ConsumableValue(self.initial_value)
        self.assertFalse(consumable.consumed)
        _ = consumable.value
        self.assertTrue(consumable.consumed)
        consumable.value = self.initial_value
        self.assertTrue(consumable.consumed)


if __name__ == '__main__':
    unittest.main()
