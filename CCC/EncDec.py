"""
get a input from user - done
reverse the input - done
replace vowels with number from 0-4 - done
add aca to the end of the string - done
create a function that decrypts - done
contionusly ask user for option one or two - done
if option 1 then encrypt if option two decrypt - done
"""
def encryption(userin):
    # Step 1 - Reverse the user input
    reversed = userin[::-1]
    print ("Reversed: {}".format(reversed))

    # Step 2 - Replace AEIOU with 01234
    output = ""
    for ch in reversed:
        if ch in "Aa":
            ch = '0'
        elif ch in "Ee":
            ch = '1'
        elif ch in "Ii":
            ch = '2'
        elif ch in "Oo":
            ch = '3'
        elif ch in "Uu":
            ch = '4'
        else:
            ch = ch
        output += ch
    
    print ("Replaced: {}".format(output))

    # Step 3 - To append "aca" to the end of message
    output += "aca"
    print ("Appended: {}".format(output))

def decryption(userin):
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

while(1):
    userin = input("Enter your input text: ")
    choice = int (input("Enter your choice - 1 (Encrypt) 2 (Decrypt): "))
    if choice == 1:
        encryption(userin)
    elif choice == 2:
        decryption(userin)
    else:
        print("Invalid input. ONLY 1 or 2 accepted.")