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
    'MX̅CDXXII',
    'X̅MV̅DCCLXIX',
    'X̅L̅MV̅CXI',
    'L̅X̅X̅MV̅XXII',
    'X̅C̅MV̅DCCCLXXXVIII',
    'C̅C̅X̅C̅V̅MMMDCCXCIII',
    'D̅C̅C̅L̅X̅X̅MV̅XXII',
    'M̅M̅C̅C̅X̅C̅V̅MMMDCCXCIII',
    'M̅M̅M̅C̅M̅X̅C̅MX̅CMXCIX'
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
    8793,
    9422,
    14769,
    44111,
    74022,
    94888,
    298793,
    774022,
    2298793,
    3999999
]

#################
#   Testing     #
#################

class TestRomanConverters(unittest.TestCase):
    def test_de2ro(self):
        print('Testing some numbers...\n')
        # Test numbers in the list 
        for i in range(len(roman_numbers)):
            resultado = decimal_to_roman(decimal_numbers[i])
            print(f'Test: in[{decimal_numbers[i]}] --> spected_out[{roman_numbers[i]}] : real_out[{resultado}]')
            self.assertEqual(resultado, roman_numbers[i])

    def test_ro2de(self):
        print('\nTesting some romans... \n')
        # Test romans in the list 
        for i in range(len(roman_numbers)):
            resultado = roman_to_decimal(roman_numbers[i])
            print(f'Test: in[{roman_numbers[i]}] --> spected_out[{decimal_numbers[i]}] : real_out[{resultado}]')
            self.assertEqual(resultado, decimal_numbers[i])

##################
#      start     #
##################

if __name__ == '__main__':
    unittest.main()
    