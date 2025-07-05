def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    s = 0
    for i in data:
        if i%2 != 0:
            if i>s:
                s = i
    return s
print(find_max_odd([1, 4, 11, 8, 5]))