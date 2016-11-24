# Write a program that prints a multiplication table for numbers up to 12

limit = int(raw_input("Enter a limit for printing multiplication tables: "))
for i in range(1, limit+1):
    print "-----------------------------"
    print "Multiplication table for %d" % i
    for j in range(1, 11):
        product = j * i
        print "%d x %d = %d" % (i, j, product)
