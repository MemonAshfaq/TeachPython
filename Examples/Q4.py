# 4. Password Strength

# Take a password string as input.
# Check if it has at least 1 digit and 1 uppercase letter.
# Print "Strong" if it has both, otherwise "Weak".

#spec_char_list = "!@#$%^&*()"
password = input("Please enter password:")

upper = False
digit = False
#spec = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.isdigit():
        digit = True
#    elif ch in spec_char_list:
#        spec = True

if upper and digit: # and spec:
    print ("Strong!")
else:
    print ("Weak!")
