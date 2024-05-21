#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def element_replaced(list_1, ind, elem_to_replace):
    if ind < 0 or ind > len(list_1)-1:
        print("None")
    else:
        list_1[ind] = element_to_replace


element_replaced(list_,index,element_to_replace)
print(list_)
