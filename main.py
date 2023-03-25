#################
#   Function    #
#################

def decimal_to_roman(number):
    de2ro = {
        '1' : 'I',
        '4' : 'IV',
        '5' : 'V',
        '9' : 'IX',
        '10' : 'X',
        '40' : 'XL',
        '50' : 'L',
        '90' : 'XC',
        '100' : 'C',
        '400' : 'CD',
        '500' : 'D',
        '900' : 'CM',
        '1000' : 'M'
        }
    decimal = ['1',
               '4',
               '5',
               '9',
               '10',
               '40',
               '50',
               '90',
               '100',
               '400',
               '500',
               '900',
               '1000'
               ]

    # How it works?
    # if input number is equal to a number in the list, it's assigned
    # if not, it divide the number in 2 parts...
    # the first part, that consist in the bigger part of the number
    # example: 48 -> first part 40, second part 8
    #  the 8 then -> first part 5, second part 3, and so
    # At the end recursivity join all number parts togeher

    for i in range(len(decimal)):
        if number == int(decimal[i]):
            # print(f'number in: {number}, decimal in: {decimal[i]}')
            roman = de2ro[decimal[i]]
            number = 0
            break
        elif number < int(decimal[i]):
            # print(f'number in: {number}, decimal in: {decimal[i]}')
            roman = de2ro[decimal[i-1]]
            number = number - int(decimal[i-1])
            break
        elif number > int(decimal[-1]):
            roman = de2ro[decimal[-1]]
            number = number - int(decimal[-1])
            break
    # print(f'number return: {number}, roman return: {roman}')
    if number == 0:
        # print('Number returned successfully')
        return roman
    else:
        # print('Recursivity...')
        result = roman + decimal_to_roman(number)
    return result

# print(decimal_to_roman(int(input('Type a number: '))))