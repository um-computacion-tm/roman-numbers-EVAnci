#################
#    Imports    #
#################

import unittest
from main import decimal_to_roman

#################
#   Testing     #
#################

class TestDecimalToRoman(unittest.TestCase):
    def test_basicos(self):
        # Define basic numbers
        roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        decimal_numbers = [1,5,10,50,100,500,1000]
        # Test numbers in the list 
        for i in range(len(roman_numbers)):
            print(f'Test: in[{decimal_numbers[i]}] --> out[{roman_numbers[i]}]')
            resultado = decimal_to_roman(decimal_numbers[i])
            self.assertEqual(resultado, roman_numbers[i])

##################
#      start     #
##################

if __name__ == '__main__':
    unittest.main()