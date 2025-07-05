def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    s = 0
    ind = 0
    for i in data:
        if s < i:
            s = i
            ind = 1
        elif s == i:
            ind += 1
    return ind 
print(find_max_count([12, 12, 10, 9, 8, 5, 4, 12]))
