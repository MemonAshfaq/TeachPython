userin = input("Enter your input text: ")

# STEP 1 - To remove last 3 characters (aca)
cut = userin[0:-3]
print ("Cut: {}".format(cut))

# STEP 2 - Replace 01234 with AEIOU

output = ""
for ch in cut:
    if ch == "0":
        ch = 'A'
    elif ch == "1":
        ch = 'E'
    elif ch == "2":
        ch = 'I'
    elif ch == "3":
        ch = 'O'
    elif ch == "4":
        ch = 'U'
    else:
        ch = ch
    output += ch

print ("Replaced: {}".format(output))

# STEP 3 - Reverse it.
output = output[::-1]
print ("Reversed: {}".format(output))