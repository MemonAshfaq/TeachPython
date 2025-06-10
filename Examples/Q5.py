#5. Letter Count

#Take a sentence and a character as input.
#Count how many times that character appears in the sentence.
#(Don’t use the .count() method)

sentence = input("What's on your mind?: ")
find_ch = input("Enter a letter: ")
count = sentence.count(find_ch)

print (f"The letter '{find_ch}' appeared {count} times in \"{sentence}\"")


count = 0
for ch in sentence:
    if ch == find_ch:
        count += 1
print (f"The letter '{ch}' appeared {count} times in \"{sentence}\"")
