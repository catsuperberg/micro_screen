import unittest
from unittest import mock
from micro_screen.displayable import InputAttributes, OutputAttributes
from micro_screen.consumable_value import ConsumableReader

class TestDisplayable(unittest.TestCase):
    
    def test_size_accesible(self):
        size = 5
        mock_data = mock.MagicMock(spec=ConsumableReader)
        input = InputAttributes(size, None)
        output = OutputAttributes(size, mock_data)
        self.assertEqual(size, input.size)
        self.assertEqual(size, output.size)
        

if __name__ == '__main__':
    unittest.main()
