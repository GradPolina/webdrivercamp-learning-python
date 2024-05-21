#!/usr/bin/python3
matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]

def nested_list(matrix1):
    for row1 in matrix1:
        for row2 in row1:
            print(row2, end =' ')
        print()    
        

print(nested_list(matrix))



