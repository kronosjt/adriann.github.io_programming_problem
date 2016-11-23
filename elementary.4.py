# Write a program that asks the user for a number n and prints
# the sum of the numbers 1 to n

n = int(raw_input("Enter a number:"))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print "Sum of numbers up to %d is: %d" % (n, sum)
