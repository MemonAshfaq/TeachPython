#Q3. Clap Game

#Print numbers from 1 to n.
#If a number contains the digit 3, print "Clap!" instead of the number.
str_n = input("Enter n:")


#Method 2
for ch in str_n:
    if ch == '3':
        print ("Clap!")
    else:
        print (ch)

#Method 1
n = int(str_n[::-1])

while (n > 0):
    digit = n % 10 #1 % 10 --> 1
    if (digit == 3):
        print ("Clap!")
    else:
        print(digit)
    n = n // 10 #1 --> 0
