sentance = input("Enter a sentence: ")
vowels = "aeiou"
words = sentance.split()
pig_latin_word = []
for word in words:
    if word[0].lower() in vowels:
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + word[0] + "ay"
    pig_latin_word.append(pig_word)

translated = " ".join(pig_latin_word)
print("Pig Latin : ", translated)