def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    s = 0
    for i in data:
        if i > s:
            s = i
    return s
print(find_max([1, 2, 4, 5, 6]))
    