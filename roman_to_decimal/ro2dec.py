def roman_to_decimal(roman):
    
    # The upperbar character is a unicode type character, so when the for
    # divide the string, it gets 2 character, the normal character, and in the
    # other hand the upper bar. That causes problems, so replacing them inside
    # the program is the best solution

    if 'V̅' in roman:
        roman = roman.replace('V̅', 'U')
    elif 'X̅' in roman:
        roman = roman.replace('X̅', 'K')
    elif 'L̅' in roman:
        roman = roman.replace('L̅', 'J')
    elif 'C̅' in roman:
        roman = roman.replace('C̅', 'H')
    elif 'D̅' in roman:
        roman = roman.replace('D̅', 'G')
    elif 'M̅' in roman:
        roman = roman.replace('M̅', 'T')

    roman = roman.upper()

    ro2dec_dic = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        'U' : 5000,
        'K' : 10000,
        'J' : 50000,
        'H' : 100000,
        'G' : 500000,
        'T' : 1000000
    }

    decimal = 0
    previous = 0

    for char in roman[::-1]:
        value = ro2dec_dic[char]
        if value < previous:
            decimal -= value
        else:
            decimal += value
        previous = value
        
    return decimal