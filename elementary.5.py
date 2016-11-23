# Only multiples of three or five are considered in the sum

n = int(raw_input("Enter a number:"))
sum = 0
for i in range(1, n+1):
    if i % 3 ==0 or i % 5 == 0:
        sum = sum + i
print "Sum of numbers up to %d is: %d" % (n, sum)
