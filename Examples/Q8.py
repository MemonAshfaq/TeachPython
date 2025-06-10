#8. Mirror Letters

#Take a string input.
#Reverse the string and swap the case of each letter.
#(e.g. "AbC" becomes "cBa")



























text = input("Enter a string:")

rev_swap_text = text[::-1].swapcase()

print (rev_swap_text)

mirror = ""
for ch in text:
    if ch.isupper():
        ch = ch.lower()
    elif ch.islower():
        ch = ch.upper()
    mirror = ch + mirror

print (mirror)

