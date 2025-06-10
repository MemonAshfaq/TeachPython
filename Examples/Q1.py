# Q1. Triple Trouble
# 
# Take 3 numbers between 1 and 9.
# If their sum is greater than 15, print "Overload"
# If their sum is less than 10, print "Underload"
# Otherwise, print "Perfect"

while(True): # Keep doing this until thing inside the bracket is non-zero or TRUE
    print ("Please enter 3 numbers.")
    a = input("a:")
    b = input("b:")
    c = input("c:")

    #Convert the strings to integers
    a = int(a)
    b = int(b)
    c = int(c)

    #Add these numbers
    sum = a + b + c

    if (sum > 15):
        print ("Overload!")
        print("try again...")
    elif (sum < 10):
        print ("Underload!")
        print("try again...")
    else:
        print("Perfect")
        print("Bye")
        break
