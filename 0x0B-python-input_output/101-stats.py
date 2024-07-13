#!/usr/bin/python3
"""
This is "101-stats" module
"""


def print_data(size, st):
    print("File size: {}".format(size))

    for status, occ in sorted(st.items()):
        if occ != 0:
            print("{:d}: {:d}".format(int(status), occ))


def stats():
    """reads stdin line by line and computes metrics"""

    from sys import stdin

    status = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
    count = 1
    size = 0

    try:
        for line in stdin:
            code = line.split()[-2]
            size += int(line.split()[-1])

            if code in status:
                status[code] = status[code] + 1
            else:
                status[code] = 0

            if count != 0 and count % 10 == 0:
                print_data(size, status)

            count = count + 1

    except KeyboardInterrupt:
        print_data(size, status)
        raise
    print_data(size, status)


if __name__ == "__main__":
    stats()
