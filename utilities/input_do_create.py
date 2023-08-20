#!/usr/bin/python3
"""
this module houses all the functions that were needed
inorder to implement do_create
"""


def to_kwargs(args):
    """
    takes args in form of <key name>=<value> and converts to a dict
    of key: value
    it also properly formats them into their respective types
    (currently only float, int and string)
    TODO check what the behaviour of X= should be
    """
    kwargs = {}
    for arg in args:
        if "=" not in arg:
            continue
        split_list = arg.split('=', 1)
        key = split_list[0]
        raw_value = split_list[1]




def replace_underscores(sentence=""):
    """replaces all '_' with a space ' '"""
    return sentence.replace('_', ' ')

# test = "ahmed="
# result = test.split('=', 1)
# print(result)