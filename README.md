# Roman Numbers Converter

There are two functions, roman to decimal and decimal to roman. Each function converts one number to the other (specified by the name: one system to the other system)

## Instalation

There is no need to install, just download and use it in other programs. 
Also if you want to test you can run the test_romans.py.

For running any test, you can follow the example:

```bash
python3 ./example/directory/test_romans.py
```

To download

```bash
git clone https://github.com/um-computacion-tm/roman-numbers-EVAnci
```

## How it works

The **decimal_to_roman(number)** function recives a integer number and returns the equivalent number in the roman numeration system.

The **roman_to_decimal(roman)** function recives a string and it's converted to uppercase in case it isn't, and returns the equivalent in decimal numeration system.

## Usage

Just import the function you need to your python program, or copy it into your program.

To import copy the following:

```python
from decimal_to_roman.dec2ro import decimal_to_roman
```
or

```python
from roman_to_decimal.ro2dec import roman_to_decimal
```

## Known Issues

For now, both converters don't work with numbers bigger than 3.999.999

## Resources

The specials characters like this V̅, were taken from this [web](https://fsymbols.com/generators/lines/)

## Contributors

Universidad de Mendoza

Author: Anci V. Elio Valentino (62197)