#!/usr/bin/python3
def list_division(my_list_1: list, my_list_2: list, list_length: int) -> list:
    nlist = []
    for i in range(list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            divide = 0
            print("wrong type")
        except IndexError:
            divide = 0
            print("out of range")
        except ZeroDivisionError:
            divide = 0
            print("division by 0")
        finally:
            nlist += [divide]
    return nlist
