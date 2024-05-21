#!/usr/bin/python3

tuple_return = __import__('8_tuple_return').tuple_return
list_ = [1000, 2, 3]

result = tuple_return(list_)
print(result)

list_len, first_element = tuple_return(list_)
print(f"List len = {list_len}\nFirst element = {first_element}")
i
