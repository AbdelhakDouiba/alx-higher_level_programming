#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    ret = list(a_dictionary.items())[0]
    for item in a_dictionary.items():
        if a_dictionary[item[0]] > a_dictionary[ret[0]]:
            ret = item
    return ret[0]
