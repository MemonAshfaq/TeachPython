#Count Vowels

#Take a line of text as input.
#Print how many vowels it contains (a, e, i, o, u).
#(Don’t use the .count() method)

aeiou = "aeiouAEIOU"

sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    if ch in aeiou:
        count += 1

print(f"\"{sentence}\" has {count} vowels")

count = (   sentence.count('a') +
            sentence.count('e') +
            sentence.count('i') +
            sentence.count('o') +
            sentence.count('u') +
            sentence.count('A') +
            sentence.count('E') +
            sentence.count('I') +
            sentence.count('O') +
            sentence.count('U') 
        )

print(f"\"{sentence}\" has {count} vowels")
