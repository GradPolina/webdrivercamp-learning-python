#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = -1
def get_element(list_1, ind):
    if ind >= 0 and ind <= len(list_1):
        print("The element retrived is", list_1[ind])
    elif ind < 0 or ind > len(list_1):
        return None
get_element(list_, index)    




