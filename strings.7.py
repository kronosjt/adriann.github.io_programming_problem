# Write three functions that compute the sum of the numbers
# in a list: using a for-loop, a while-loop and recursion

def sumForLoop(n):
    """
    returns sum of elements in a list
    :param n:
    :return total:
    """

    total = 0
    for i in n:
        total += i
    return total

def sumWhileLoop(n):
    """
    returns sum of elements in a list
    :param n:
    :return total:
    """

    total = 0
    i = 0
    while i<len(n):
        total += n[i]
        i += 1
    return total

def sumRecursive(n):
    if len(n) == 1:  # base case
        return n[0]
    else:
        return n[0] + sumRecursive(n[1:])
