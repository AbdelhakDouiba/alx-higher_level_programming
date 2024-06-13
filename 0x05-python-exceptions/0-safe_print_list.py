#!/usr/bin/python3
def safe_print_list(my_list: list = [], x: int = 0):
    try:
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
        print()
        return x
    except:
        print()
        return i
