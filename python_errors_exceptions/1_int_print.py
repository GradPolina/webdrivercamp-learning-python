#!/usr/bin/python3

def int_print(value):
    try:
        print(f"{int(value):d}")
        return True
    except:
        return False    



if __name__ == "__main__":
    value = "Sun"
    if not (int_print(value)):
        print(f"{value} is not an integer")
    value = 100
    if not (int_print(value)):
        print(f"{value} is not an integer")
    value = "Webdriver Camp"
    if not (int_print(value)):
        print(f"{value} is not an integer")
