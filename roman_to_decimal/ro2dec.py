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

    # How it works?
    # first it inverts the string -> example: 'XLVI' -> 'IVLX'
    # 'I' value is 1 -> save to value
    # if value is bigger than previous then add it's value, if not substract it
    # previous = 0, value = 1 -> decimal = 1, previous = 1
    # Then again the same process
    # previous = 1, value = 5 -> decimal = 6, previous = 5
    # previous = 5, value = 50 -> decimal = 56, previous = 50
    # previous = 50, value = 10 -> decimal = 46, previous = 10

    for char in roman[::-1]:
        if char in ro2dec_dic: 
            value = ro2dec_dic[char]
            if value < previous:
                decimal -= value
            else:
                decimal += value
            previous = value
        else:
            return None
        
    return decimal