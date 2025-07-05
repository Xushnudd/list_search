def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    s = 0
    for i in data:
        if i%2 == 0:
            if i>s:
                s = i
    return s
print(find_max_even([1, 4, 3, 8, 5]))
