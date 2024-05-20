#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
list_copy = list_.copy()
index = 1
element_to_replace = 5
def element_replaced(list_1, ind, elem_to_replace):
    list_1[ind] = element_to_replace


element_replaced(list_,index,element_to_replace)
print("Copy: ", list_)
print("Origin: ", list_copy)
