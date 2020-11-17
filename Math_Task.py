def maxi_num(my_list):

    maxi_val = my_list[0]
    for a in my_list:
        if a > max_val:
            max_val = a

    return maxi_val
#************************************************************************************
a = [8, 50, 11, 72, 9, 3, 52, 32, 21]

def decend_sorted(a):

    b = sorted(a)
    return b[::-1]

print(maxi_num(a))