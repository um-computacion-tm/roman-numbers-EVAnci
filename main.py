#################
#   Function    #
#################

def roman_basic(number):
    num = {
        '1' : 'I',
        '4' : 'IV',
        '5' : 'V',
        '9' : 'IX',
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