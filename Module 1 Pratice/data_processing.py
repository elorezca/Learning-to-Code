 
# sentence = input("Please enter a sentence you would like capitalized: ")

# sentence_formatted = sentence.upper()

# print(sentence_formatted)

# sentence2 = input("Please type a paragrah and I will count how many words there are: ")

# print(f"This sentence has",len(sentence2.split()), "words")

# sentence3 = input("Please enter a string: ")

# res = isinstance(sentence3, int)

# print(str(res))

# sentence4 = input("Please enter a sentence: ").replace("a", "o")

# print(sentence4)

sentence5 = input("Please enter your name: ")

space1 = sentence5.find(' ')

newtext = sentence5[0].capitalize() + sentence5[space1+1].capitalize()

print(f"Your Initials are: {newtext}")

# sentence6 = input("Please enter another string: ")

# print(f"The length of your string is: ", (len(sentence6)))