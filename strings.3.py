# Write a function that checks whether an element occurs in a list.

def existInList(inputString, inputList):
    """
    Returns true if inputString exists in inputList
    """
    for i in inputList:
        if i == inputString:
            return True
        else:
            return False


def testExistInList():
    string1 = 'a'
    list1 = ['a', 'b', 'c', 'd']
    answer = existInList(string1, list1)
    if answer == True:
        print "'%s' exists in the given list" % (string1)
    else:
        print "'%s' does not exist in the list" % (string1)