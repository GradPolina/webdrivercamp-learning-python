#!/usr/bin/python3

def tuple_return(arg):
    len_arg = len(arg)
    if len(arg) == 0:
        first_el = None
    else:
        first_el = arg[0]
    return len_arg, first_el    
