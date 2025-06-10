#Q2. Backwards Number

#Take a 3-digit number and print the number reversed.
#(Do not use string indexing like [1] or [::-1])

while(True):
    # Get a 3-digit string
    n = input("Enter a 3-digit number:")
    #print (n[::-1]) 

    # Convert it to a 3-digit number
    n = int (n)

    if (n < 0):
        neg = True
        n = abs(n)

        # Check if it is exactly 3 digits
    valid = False
    if ((n >= 100) and (n <= 999)):
        valid = True
    else:
        valid = False

    if (valid):
        print("valid...")
    else:
        print("invalid... Try again...")
        continue

    h = n // 100
    t = (n // 10) % 10
    u = n % 10

    rev_n = u * 100 + t * 10 + h

    if (neg):
        rev_n = rev_n * -1
    
    print ("Reversed:", rev_n)