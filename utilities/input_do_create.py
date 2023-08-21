#!/usr/bin/python3
"""
this module houses all the functions that were needed
inorder to implement do_create
"""
from datetime import datetime


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
        processed_value = process_value(raw_value)
        if processed_value is None:
            continue
        if type(processed_value) is str:
            processed_value = processed_value.replace('"', '')
        kwargs[key] = processed_value
    return kwargs


def process_value(raw_value):
    """
    converts the raw value into the datatype we need it in
    (currently only float, int and string)
    """
    processed_value = None
    if raw_value[0] == '"':
        processed_value = process_string(raw_value)
    elif '.' in raw_value:
        processed_value = float(raw_value)
    else:
        processed_value = int(raw_value)
    return processed_value


def process_string(raw_string):
    """
    escapes all quotes except the start and end.
    """
    cut_string = raw_string[1:]
    if raw_string[-1] == '"':
        cut_string = cut_string[:-1]
    cut_string.replace('"', '\"')
    processed_string = "\"" + cut_string + "\""
    processed_string = replace_underscores(processed_string)
    return processed_string


def replace_underscores(sentence=""):
    """replaces all '_' with a space ' '"""
    return sentence.replace('_', ' ')
