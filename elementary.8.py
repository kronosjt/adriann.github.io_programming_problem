# Write a program that prints all prime numbers

def isPrime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True # 2 & 3 are prime
    elif number % 2 == 0 or number % 3 == 0:
        return False
    # the next section checks for divisors of the form 6k+-1
    # i.e. 5, 7, 11, 13, 17, 19, 23, 25 and so on
    # other numbers can be skipped because if they are divisors
    # then 2 and/or 3 are also divisors
    else:
        divisor = 5
        while divisor ** 2 <= number: # divisors only upto sqrt of number
            if number % divisor == 0 or number % (divisor + 2) == 0:
                return False
            divisor = divisor + 6
        else:
                return True

number = 1
while number > 0:
    result = isPrime(number)
    if result == True:
        print number
    number = number + 1
