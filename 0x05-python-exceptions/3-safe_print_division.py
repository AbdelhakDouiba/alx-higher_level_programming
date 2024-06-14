#!/usr/bin/python3
def safe_print_division(a: int, b: int) -> int:
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
