n = input("Enter a number: ")
n = int(n)

# Make sure we have got 3-digits
if (n >= 100) and (n <= 999):
    print ("Yay! 3 digits")
else:
    print ("Try again!")

h = n // 100 #1
t = ( n // 10 ) % 10 #2
u = n % 10 #3

print (h)
print (t)
print (u)

reversed = u*100 + t*10 + h

print("Reversed:{}".format(reversed))

print("Reversed: ")