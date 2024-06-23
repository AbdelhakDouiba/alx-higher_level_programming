#!/usr/bin/python3
'''
This is 5-text_indentation Module
text_indentation - prints a text with 2 new lines after
                   each of these characters: ., ? and :
'''


def text_indentation(text: str):
    '''prints a text with 2 new lines after each of
       these characters: ., ? and :

        Args:
            text: input text
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 1
    for char in text:
        if flag == 1 and char == " ":
            continue
        else:
            flag = 0
        print(char, end="")
        if char in [".", "?", ":"]:
            print("\n")
        if char == "\n" or char in [".", "?", ":"]:
            flag = 1
