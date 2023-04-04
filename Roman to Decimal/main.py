def roman_to_decimal(roman):
    ro2de = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    for i in ro2de:
        if i == roman:
            