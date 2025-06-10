sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

#METHOD 1
for ch in sentence:
    if ch in vowels:
        count += 1
    else:
        pass

print ("There are {} vowels in {}".format(count, sentence))

count = 0 

#METHOD 2
for v in vowels:
    count += sentence.count(v)
print ("There are {} vowels in {}".format(count, sentence))
