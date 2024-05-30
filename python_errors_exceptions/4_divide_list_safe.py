#!/usr/bin/python3

def divide_list_safe(list_1, list_2, list_len):
    list_result = []
    for i in range(list_len):
        try: 
            result = (list_1[i]/list_2[j])
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
            result = 0
         finally:
            new_list.append(result)

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
