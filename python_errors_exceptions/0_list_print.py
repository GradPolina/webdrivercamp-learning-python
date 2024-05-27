#!/usr/bin/python3

def list_print(lst=[], i=0):
    count = 0
    try:
        for index in range(i):
            print(lst[index], end=' ')
            count += 1
    except IndexError:
        pass
    print()  
    return count

if __name__ == "__main__":
    list_ = [1, 2, 3, 5, 5, 6, 9]
    count = list_print(list_, 4)
    print(f"Count: {count:d}")
    count = list_print(list_, 7)
    print(f"Count: {count:d}")
    count = list_print(list_, 9)
    print(f"Count: {count:d}")
