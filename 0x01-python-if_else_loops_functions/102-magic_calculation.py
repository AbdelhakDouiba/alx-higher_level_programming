#!/usr/bin/bash

def magic_calculation(a, b, c):
    '''
        magic_calculation - magic
        Return: magic
    '''
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
