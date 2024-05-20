#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
    print(some_string[1:2] + some_string[4] + some_string[6] + some_string[8:10], sep = '\n')
    print (some_string[13:29] + some_string[30])


remove_char(string)
