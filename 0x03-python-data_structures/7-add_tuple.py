#!/usr/bin/python3
def add_tuple(tuple_a: tuple = (), tuple_b: tuple = ()) -> tuple:
    if len(tuple_a) == 0:
        a = (0, 0)
    elif len(tuple_a) == 1:
        a = tuple_a + (0, )
    else:
        a = tuple_a[:2]
    if len(tuple_b) == 0:
        b = (0, 0)
    elif len(tuple_b) == 1:
        b = tuple_b + (0, )
    else:
        b = tuple_b[:2]
    return (a[0] + b[0], a[1] + b[1])
