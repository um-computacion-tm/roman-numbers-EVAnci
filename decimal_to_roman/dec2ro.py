#################
#   Function    #
#################

def decimal_to_roman(number):
    de2ro = {
        1 : 'I',
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10 : 'X',
        40 : 'XL',
        50 : 'L',
        90 : 'XC',
        100 : 'C',
        400 : 'CD',
        500 : 'D',
        900 : 'CM',
        1000 : 'M',
        4000 : 'MV̅',
        5000 : 'V̅',
        9000 : 'MX̅',
        10000 : 'X̅',
        40000 : 'X̅L̅',
        50000 : 'L̅',
        90000 : 'X̅C̅',
        100000 : 'C̅',
        400000 : 'C̅D̅',
        500000 : 'D̅',
        900000 : 'C̅M̅',
        1000000 : 'M̅'
        }

    # How it works?
    # if input number is equal to a number in the dictionary, it's assigned
    # if not, it divide the number in 2 parts...
    # the first part, that consist in the bigger part of the number
    # example: 48 -> first part 40, second part 8
    #  the 8 then -> first part 5, second part 3, and so
    # if the number is bigger than the last number in the dictionary, that 
    # number will be selected (the "last" variable contains it)
    # At the end recursivity join all number parts togeher

    prev = 0
    last = 1000000

    for dec in de2ro:
        if number == dec:
            roman = de2ro[dec]
            number = 0
            break
        elif number < dec:
            roman = de2ro[prev]
            number = number - prev
            break
        elif number > last:
            roman = de2ro[last]
            number = number - last
            break
        prev = dec

    # print(f'number return: {number}, roman return: {roman}')
    if number == 0:
        # print('Number returned successfully')
        return roman
    else:
        # print('Recursivity...')
        result = roman + decimal_to_roman(number)
    return result



# To try a number you want, uncomment the start section, and execute:

#############
#   start   #
#############

# if __name__ == '__main__':
#     print(decimal_to_roman(int(input('Type a number: '))))