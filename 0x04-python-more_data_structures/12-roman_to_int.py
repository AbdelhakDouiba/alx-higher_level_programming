#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dict = {
                    'M': 1000,
                    'D': 500,
                    'C': 100,
                    'L': 50,
                    'X': 10,
                    'V': 5,
                    'I': 1
                 }
    result = 0
    for char in roman_string:
        result += roman_dict[char]
    return result
