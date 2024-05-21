#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 0

def get_element(list_1, ind):
    if ind < 0 or ind > len(list_1)-1:
        print("None")
    else:    
        print("The element retrived is", list_1[ind])


get_element(list_, index)
