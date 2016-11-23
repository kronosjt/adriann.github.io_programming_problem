#Write a program that asks the user for a number n and gives him the
#possibility to choose between computing the sum and computing the product of 1-n

n = int(raw_input("Enter a number:"))
answer = raw_input("Do you want to compute sum (s) or product (p)? ")
if answer == 's':
    summed = 0
    for i in range(1, n+1):
        summed = summed + i
    print "Sum of numbers up to %d is: %d" % (n, summed)
elif answer == 'p':
    product = 1
    for i in range(1, n+1):
        product = product * i
    print "Product of numbers up to %d is: %d" % (n, product)
else:
    print "You chose wrong option"
