#!/usr/bin/python3
def safe_print_list_integers(my_list: list = [], x: int = 0) -> int:
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except (ValueError, TypeError):
            pass
    print()
    return count
