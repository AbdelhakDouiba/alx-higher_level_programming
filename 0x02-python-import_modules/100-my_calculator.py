#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv) - 1
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    op_1 = int(sys.argv[1])
    op_2 = int(sys.argv[3])
    if sys.argv[2] == '+':
        print('{} + {} = {}'.format(op_1, op_2, add(op_1, op_2)))
    elif sys.argv[2] == '-':
        print('{} - {} = {}'.format(op_1, op_2, sub(op_1, op_2)))
    elif sys.argv[2] == '*':
        print('{} * {} = {}'.format(op_1, op_2, mul(op_1, op_2)))
    elif sys.argv[2] == '/':
        print('{} / {} = {}'.format(op_1, op_2, div(op_1, op_2)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
