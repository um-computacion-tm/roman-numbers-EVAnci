#################
#    Imports    #
#################

import unittest
from decimal_to_roman.dec2ro import decimal_to_roman
from roman_to_decimal.ro2dec import roman_to_decimal

################################
#    Hardcoded test numbers    #
################################

roman_numbers = [
    'I',
    'IV',
    'V',
    'IX',
    'X',
    'XL',
    'L',
    'XC',
    'C',
    'CD',
    'D',
    'CM',
    'M',
    'III',
    'VIII',
    'XVIII',
    'XIX',
    'XXIV',
    'XXXIII',
    'XXXVII',
    'XLIV',
    'LVI',
    'LXIII',
    'LXXVII',
    'LXXXIII',
    'XCIX',
    'CXXIV',
    'CCCLXII',
    'CDXV',
    'DXII',
    'DCLXXXII',
    'DCCCXLIV',
    'CMXCIX',
    'MDCCCLXXXVIII',
    'MMMCDLXVII',
    'MV̅DXXV',
    'V̅DCLXXVIII',
    'V̅MMMDCCXCIII', 
]

decimal_numbers = [
    1,
    4,
    5,
    9,
    10,
    40,
    50,
    90,
    100,
    400,
    500,
    900,
    1000,
    3,
    8,
    18,
    19,
    24,
    33,
    37,
    44,
    56,
    63,
    77,
    83,
    99,
    124,
    362,
    415,
    512,
    682,
    844,
    999,
    1888,
    3467,
    4525,
    5678,
    8793
]

#################
#   Testing     #
#################

class TestRomanConverters(unittest.TestCase):
    def test_de2ro(self):
        print('Testing some numbers...\n')
        # Test numbers in the list 
        for i in range(len(roman_numbers)):
            print(f'Test: in[{decimal_numbers[i]}] --> out[{roman_numbers[i]}]')
            resultado = decimal_to_roman(decimal_numbers[i])
            self.assertEqual(resultado, roman_numbers[i])

    def test_ro2de(self):
        print('\nTesting some romans... \n')
        # Test romans in the list 
        for i in range(len(roman_numbers)):
            print(f'Test: in[{roman_numbers[i]}] --> out[{decimal_numbers[i]}]')
            resultado = roman_to_decimal(roman_numbers[i])
            self.assertEqual(resultado, decimal_numbers[i])

##################
#      start     #
##################

if __name__ == '__main__':
    unittest.main()
    