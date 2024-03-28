text="The quick brown fox jumps over the lazy dog. The dog barks."
text_list = text.split()
for word in text_list:
    temp_word = ''
    for char in word:
        if char.isalpha():
            if char.isalpha():
                temp_word = temp_word + char
    word = temp_word
    print(word)
        
