def palindrome(word, ind):
    current_ind = ind - 1
    new_word = ''
    if current_ind == -1:
        new_word += "|" + word[current_ind]
        word += new_word
    else:
        new_word += word[current_ind]
        word += new_word

    special_symbol_ind = word.index("|")

    if len(word[0:special_symbol_ind]) == len(word[special_symbol_ind + 1:]):
        if word[0:special_symbol_ind] == word[special_symbol_ind + 1:]:
            return f"{word[0:special_symbol_ind]} is a palindrome"
        else:
            return f"{word[0:special_symbol_ind]} is not a palindrome"
    if current_ind == -1:
        return palindrome(word, ind - 3)
    else:
        return palindrome(word, ind - 2)


print(palindrome("peter", 0))
