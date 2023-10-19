import unittest
from unittest import mock
from micro_screen.consumable_value import ConsumableValue, ConsumableReader
from micro_screen.displayable import OutputAttributes

class TestClass():
    def __init__(self):
        self.data = 'bonjour'

class TestOutputAttributes(unittest.TestCase):
    
    def test_init(self):
        valid_data = ConsumableReader(ConsumableValue('valid'))
        mock_data = mock.MagicMock(spec=ConsumableReader)
        invalid_data = 'invalid'        
        print(type(mock_data))
        print(type(valid_data))
        OutputAttributes(size=10, data=valid_data)
        OutputAttributes(size=10, data=mock_data)
        with self.assertRaises(TypeError):
            OutputAttributes(size=10, data=invalid_data)
        

if __name__ == '__main__':
    unittest.main()
