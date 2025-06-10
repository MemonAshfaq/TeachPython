sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

count = 0

for i in sentence:
    if i == letter:
        count += 1
    else:
        pass


print ("The letter {} appears for {} times in {}".format(letter, count, sentence))