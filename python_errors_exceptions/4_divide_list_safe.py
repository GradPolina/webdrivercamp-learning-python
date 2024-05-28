#!/usr/bin/python3

def divide_list_safe(list_1, list_2, list_len):
    list_result = []
    for i in range(list_len):
        try: 
            if i >= len(list_1) or i >= len(list_2):
                print("out of range")
                list_result.append(0)
                continue
            else:
                list_result.append(list_1[i]/list_2[j])
            try:       
                res=list_1[i]/list_2[i]
             except TypeError:
                 print("wrong type")
                 list_result.append(0)
                 continue

         except ZeroDivisionError:
               print("Division by 0")
               list_result.append(0)
         finally:
               pass

         return list_sesult

  


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
