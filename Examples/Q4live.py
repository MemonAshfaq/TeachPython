password = input("Enter a password: ")

has_digit = False
has_upper = False
has_spec = False

spec_list = "!@#$%^&*()"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_digit = True
    elif ch in spec_list:
        has_spec = True

if has_digit and has_upper and has_spec:
    print ("Strong!")
else:
    print ("Weak!")
