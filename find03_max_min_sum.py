def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    max = 0
    min = 0
    for i in data:
        if max<i:
            max = i
        if min == 0:
            min = i
        elif min>i:
            min = i
    return max + min
print(find_max_min_sum([12, 11, 10, 5, 7, 9, 6, 4, 15, 0]))
