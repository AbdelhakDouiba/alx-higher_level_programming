#!/usr/bin/python3
'''
This is "100-my_int" Module
'''


class MyInt(int):
    '''MyInt - a class that inherits from int'''

    def __eq__(self, other):
        '''equality check'''

        if self > other or self < other:
            return True
        return False

    def __ne__(self, other):
        '''equality check'''

        if not self < other and not self > other:
            return True
        return False
