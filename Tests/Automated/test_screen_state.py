import unittest
from micro_screen.screen_state import ScreenState, ScreenStateReader, InputField, DynamicField
from micro_screen.line import Line
from micro_screen.displayable import InputAttributes, OutputAttributes
from micro_screen.consumable_value import ConsumableValue, ConsumableReader

class TestScreenState(unittest.TestCase):
    consumables = [
        ConsumableReader(ConsumableValue(1)),
        ConsumableReader(ConsumableValue(2)),
        ConsumableReader(ConsumableValue(3))
    ]
    callbacks = [
        lambda: print('1'),
        lambda: print('2'),
        lambda: print('3'),
        lambda: print('4')
    ]
    inputs = [
        InputAttributes(5, callbacks[0]),
        InputAttributes(4, callbacks[1]),
        InputAttributes(3, callbacks[2]),
        InputAttributes(2, callbacks[3])
    ]
    outputs = [
        OutputAttributes(1, consumables[0]),
        OutputAttributes(2, consumables[1]),
        OutputAttributes(3, consumables[2])
    ]    
    initial_lines = [
        Line(['one', inputs[0], 'two', outputs[0]]),
        Line(['three', inputs[1], '|', inputs[2], 'four', outputs[1], '|', outputs[2]]),
        Line([inputs[3], 'five']),
        Line([])
    ]
    
    expected_static_lines = [
        'one     two ',
        'three    |   four  |   ',
        '  five',
        ''
    ]    
    expected_dynamic_fields = [
        DynamicField([0, 11], 1, consumables[0]),
        DynamicField([1, 17], 2, consumables[1]),
        DynamicField([1, 20], 3, consumables[2])
    ]    
    expected_input_fields = [
        InputField([0, 3], 5, callbacks[0]),
        InputField([1, 5], 4, callbacks[1]),
        InputField([1, 10], 3, callbacks[2]),
        InputField([2, 0], 2, callbacks[3])
    ]
    
    def test_init_from_lines(self):
        state = ScreenState(self.initial_lines)
        self.assertEqual(0, state.selected_input)
        self.assertEqual('', state.input_string)
        self.assertEqual(self.expected_static_lines, state._static_lines)
        self.assertEqual(self.expected_dynamic_fields, state._dynamic_fields)
        self.assertEqual(self.expected_input_fields, state._inputs)
        
    def test_readable_raises_on_writes(self):   
        state = ScreenState(self.initial_lines)
        reader = ScreenStateReader(state)
        with self.assertRaises(AttributeError):
            reader.selected_input = None
        with self.assertRaises(AttributeError):
            reader.input_string = None
        with self.assertRaises(AttributeError):
            reader.static_lines = None
        with self.assertRaises(AttributeError):
            reader.dynamic_fields = None
        with self.assertRaises(AttributeError):
            reader.inputs = None
            
    def test_assert_lists_are_equivalent(self):
        lambdas = [lambda: print("hello"), lambda: print("world")]
        list1 = [InputField((100, 100), 10, lambdas[0]),
                 InputField((200, 200), 20, lambdas[1])]
        list2 = [InputField((100, 100), 10, lambdas[0]),
                 InputField((200, 200), 20, lambdas[1])]

        self.assertEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
