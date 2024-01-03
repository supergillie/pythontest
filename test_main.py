import unittest
from unittest.mock import patch
import main

class TestPrintHi(unittest.TestCase):
    #The argument 'builtins.print' tells patch exactly what to replace with a mock object.
    # In this case, it's the built-in print function.
    @patch('builtins.print')
    def test_print_hi(self, mock_print):
        main.print_hi('Apa')
        mock_print.assert_called_with('Hello Apa')

if __name__ == '__main__':
    unittest.main()