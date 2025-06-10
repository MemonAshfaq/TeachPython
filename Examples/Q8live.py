#Q8. Mirror Letters

#Take a string input.
#Reverse the string and swap the case of each letter.
#(e.g. "AbC" becomes "cBa")

userinput = input ("Enter a string: ")

revinput = userinput[::-1]

mirror = ""

for ch in revinput:
    if ch.isupper():
        ch = ch.lower() #a
    elif ch.islower():
        ch = ch.upper()
    else:
        pass
    mirror += ch #"aBc1@D"

print (mirror)