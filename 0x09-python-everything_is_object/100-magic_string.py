#!/usr/bin/python3
def magic_string(loc={"N": 0}):
    loc["N"] += 1
    return str("BestSchool, " * loc["N"])[:-2]
