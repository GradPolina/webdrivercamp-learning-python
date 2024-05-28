#!/usr/bin/python3

def divide_list_safe(list_1, list_2, list_len):
    try: 
        if len(list_1) == len(list_2):
            for i in range(len(list_1)):
                list_len.append(list_1[i]/list_2[i])
        else:
            for i in range(len(list_1)):
                print("out of range")
                list_len.append(0)

    except ZeroDivisionError:
        print("Division by 0")
    finally:
        pass
    return list_len

  


if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
