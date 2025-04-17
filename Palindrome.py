def is_Palindrome(text):
    normalized_text = text.replace(" ", "").lower()

    if normalized_text == normalized_text[::-1]:
        return True
    else:
        return False


input_text = input("Enter a word or Phrase: ")

if is_Palindrome(input_text):
    print(f"'{input_text}' is a palindrome.")
else:
    print(f"'{input_text}' is not a palindrome.")
