#!/usr/bin/python3
def list_division(my_list_1: list, my_list_2: list, list_length: int) -> list:
    nlist = []
    for i in range(list_length):
        divide = 0
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            nlist += [divide]
    return nlist
