# Write a function that returns the elements on odd positions in a list.

def oddElements(inputList):
    """
    Returns odd elements from a list
    :param inputList:
    :return oddElementsList:
    """
    oddElementsList = list([])

    for i in range(0, len(inputList)-1, 2):
        oddElementsList.append(inputList[i])

    return oddElementsList


def testOddElements():
    answer = oddElements([1,2,3,4,5,6,7,8,9,10])
    print answer