original = input("Please enter a sentence: ").strip().lower()

words = original.split()

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "ium"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        letter_index = 0
        while word[letter_index] not in "aeiou":
            vowel_pos = vowel_pos + 1
            letter_index = letter_index + 1
        # teacher's version:
        # for letter in word:
        #     if letter not in "aeiou":
        #         vowel_pos = vowel_pos + 1
        #     else:
        #         break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "um"
        new_words.append(new_word)
                
output = " ".join(new_words) 
print(output)
