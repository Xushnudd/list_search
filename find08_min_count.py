def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    s = 0
    ind = 0
    for i in data:
        if s == 0:
            s = i
        elif s > i:
            s = i
            ind = 1
        elif s == i:
            ind += 1
    return ind 
print(find_min_count([12, 12, 10, 9, 8, 5, 4, 4, 4, 12]))
