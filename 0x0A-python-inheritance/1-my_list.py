#!/usr/bin/python3
'''
This is "1-my_list" Module
'''


class MyList(list):
    '''An inherited class from list'''

    def print_sorted(self):
        '''prints the list, but sorted (ascending sort)'''

        print(sorted(self))
