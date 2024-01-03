import unittest

def print_hi(name):
    return f'Hi, {name}'  # Adjust this function as needed

class TestPrintHi(unittest.TestCase):
    def test_print_hi(self):
        # Update the expected output to match what print_hi actually returns
        self.assertEqual(print_hi('Monkey'), 'Hi, Monkey')

if __name__ == '__main__':
    unittest.main()
