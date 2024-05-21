#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]
my_tuple = []
for item in my_list:
    if item % 2 == 0:
        my_tuple.append(True)
    else:
        my_tuple.append(False)
my_tuple1 = tuple(my_tuple)        
print(my_tuple1)        

