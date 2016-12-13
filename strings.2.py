# Write function that reverses a list


def reverseList(input_list):
    new_list = list([])
    for i in range(len(input_list)-1, -1, -1):  # Start at last element, decrement by -1 till you get to 0th
        new_list.append(input_list[i])

    return new_list

def testReverseList():
    answer = reverseList([1,2,3,4,5,'a','b','c','d'])
    print answer



