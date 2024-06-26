#!/usr/bin/python3
import sys


def safe_print_integer_err(value) -> bool:
    try:
        print("{:d}".format(value))
        return True
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
