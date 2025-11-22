def even_odd(x):
    '''
    param 1: take value from user as list of integers
    type(param-1): list

    return: check number is even or odd
    type(return): two lists - even and odd
    '''
    odd = []
    even = []
    for i in x:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd