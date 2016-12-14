# Write a function that tests whether a string is a palindrome.

def isPalindrome(s):
    """
    checks if a string is a palindrome
    :param s:
    :return:
    """

    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


