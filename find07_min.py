def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    s = 0
    for i in data:
        if s == 0:
            s = i
        elif i<s:
            s = i

    return s
print(find_min([12, 34, 556, 7, 634, 2]))