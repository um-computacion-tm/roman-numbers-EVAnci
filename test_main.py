#################
#    Imports    #
#################

import unittest
from main import decimal_to_roman

#################
#   Testing     #
#################

class TestDecimalToRoman(unittest.TestCase):
    def test_numbers(self):
        print('Testing some numbers...')
        # Define numbers
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
            'MMMCDLXVII'
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
            3467
        ]
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