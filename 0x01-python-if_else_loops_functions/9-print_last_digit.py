#!/usr/bin/bash

def print_last_digit(number: int) -> int:
    '''
        print_last_digit - prints the last digit of a number.
        Return: the last digit
    '''
    print(f'{abs(number) % 10}', end='');
    return abs(number) % 10
