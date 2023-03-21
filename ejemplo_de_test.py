########################################################
#             Decimal to roman Converter               #   
########################################################

# Buscamos una mejor forma de hacerlo
# Agregamos mas cosas

#################
#   Imports     #
#################

import unittest

#################
#   Function    #
#################

def roman_basic(number):
    num = {
        '1' : 'I',
        '5' : 'V',
        '10' : 'X',
        '50' : 'L',
        '100' : 'C',
        '500' : 'D',
        '1000' : 'M'
    }
    return num[str(number)]

def decimal_to_roman(decimal):
    if roman_basic(decimal) == None:
        print('not a basic number')
    else:
        return roman_basic(decimal)

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
            resultado = decimal_to_roman(decimal_numbers[i])
            self.assertEqual(resultado, roman_numbers[i])

#################
#      main     #
#################

if __name__ == '__main__':
    unittest.main()