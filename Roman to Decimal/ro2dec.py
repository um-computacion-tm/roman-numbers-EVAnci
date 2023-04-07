def roman_to_decimal(roman):
    roman = roman.upper()
    ro2dec_dic = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
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