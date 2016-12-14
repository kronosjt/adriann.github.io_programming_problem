# Write a function that computes the running total of a list.

def calculateListSum(inputList):
    """
    Calculates the sum of elements in a list
    :param inputList:
    :return: total
    """

    total = 0
    for i in inputList:
        total += i
    return total

def testCalculateListSum():
    answer = calculateListSum([1,2,3,4,5,6,7,8])
    print answer