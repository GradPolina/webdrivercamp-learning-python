#!/usr/bin/python3

def calc_weight(list_=[]):
    if len(list_) == 0:
        return 0

    ij_sum = 0
    j_sum = 0

    for i, j in list_:
        ij_sum += i*j
        j_sum += j

    if j_sum == 0:
        return 0
    
    return ij_sum / j_sum  
        



if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
