def word_counter():
    sentence = input("Enter a sentence : ")
    words = sentence.split()
    num_words = len(words)
    num_chars = len(sentence.replace(" ", ""))
    print(f"Number of words : {num_words}")
    print(f"Number of charaters (Excluding space): {num_chars}")


word_counter()
