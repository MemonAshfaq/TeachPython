#6. Digit Sum

#Take a number and print the sum of its digits.

number = input("Enter a number: ")

number = int (number)

sum = 0
while (number > 0):
    digit = number % 10 #3 #2 #1
    sum += digit #3 #5 #6
    number //= 10 #12 #1 #0

print (f"Sum: {sum}")