#!/usr/bin/python3
def safe_print_list(my_list: list = [], x: int = 0):
    try:
        num = 0
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
            num = num + 1
    except IndexError:
        pass
    print()
    return num
