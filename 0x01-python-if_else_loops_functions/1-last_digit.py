#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = -(abs(number) % 10)
else:
    last = number % 10
print('Last digit of {} is {}'.format(number, last), end=' ')
if last == 0:
    print('and is 0')
elif last > 5:
    print('and is greater than 5')
elif last < 6:
    print('and is less than 6 and not 0')
