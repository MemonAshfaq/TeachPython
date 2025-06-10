#9. Tally Score

#Take a string with only + and - characters.
#Each + adds 1 point, each - subtracts 1 point.
#Print the final score.

while(1):
    text = input("Enter a string of ONLY + and -:")

    valid = True
    for ch in text:
        if ch != '+' and ch != '-':
            valid = False

    sum = 0
    if valid == True:
        for ch in text:
            if ch == '+':
                sum += 1
            elif ch == '-':
                sum -= 1
        print (sum)
    else:
        print ("Enter a valid string.")