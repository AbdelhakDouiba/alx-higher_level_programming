#!/usr/bin/python3
def divisible_by_2(my_list: list = []) -> list:
    multiple_of_2 = []
    for i in my_list:
        if i % 2 == 0:
            multiple_of_2 += [True]
        else:
            multiple_of_2 += [False]
    return multiple_of_2
