def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    s = 0
    ind = 0
    for i in data:
        if i%2 == 0:
            if s == 0:
                s = i
            elif s > i:
                s = i
                ind = 1
            elif s == i:
                ind += 1
    return ind 
print(find_min_even([12, 12, 10, 9, 8, 5, 4, 4, 4, 12]))


