def exitor():
    exitor_ans = input("\n(1) Check more text (2) Exit\n").lower()
    if exitor_ans in ('1', "check more text"):
        return True
    else:
        return False


while True:
    tocheckfor = list(input("Enter the text that you would like to check for vowels and consonants\n").lower())
    y_isvowel = input("\nWould you like 'y' to be considered a vowel? (1) Yes (2) No\n").lower()
    if y_isvowel in ('1', "yes", 'y'):
        vowels = "aeiouy"
        consonants = "bcdfghjklmnpqrstvwxz"
    else:
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
    print("\nVowels: ", len([x for x in tocheckfor if x in vowels]))
    print("Consonants: ", len([x for x in tocheckfor if x in consonants]))
    exitor_ans = exitor()
    if not exitor_ans:
        break