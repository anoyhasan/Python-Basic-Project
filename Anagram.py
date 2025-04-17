def anagram():
    word1 = input("Enter the first word : ")
    word2 = input("Enter the second word : ")

    word1.lower()
    word2.lower()

    sorter1 = sorted(word1)
    sorter2 = sorted(word2)

    if sorter1 == sorter2:
        print("They are anagrams!")
    else:
        print("They are not anagrams.")


anagram()
