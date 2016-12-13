#  Write a function that returns the largest element in a list

def largestNumber(number):
    """
    Returns the largest number in a list
    """

    largest = number[0]
    counter = 1
    while counter<len(number):
        if number[counter] > largest:
            largest = number[counter]
        counter += 1
    return largest




def testLargestNumber():
    testList = [1, 2, 73, 4, 500, 6, 1744]
    answer = largestNumber(testList)
    print answer
