#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    char = i
    if i % 2 != 0:
        char -= 32
    print("{}".format(chr(char)), end="")
