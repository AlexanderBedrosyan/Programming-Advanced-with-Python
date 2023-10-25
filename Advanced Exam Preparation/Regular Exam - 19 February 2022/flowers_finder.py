from collections import deque


def is_winner(needed_words):
    for key, value in needed_words.items():
        if value == "":
            return key


vowels = deque(ch for ch in input().split(' '))
consonants = deque(ch for ch in input().split(' '))

needed_words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}

while vowels and consonants:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    for key in needed_words.keys():
        if first_vowel in key:
            new_word = needed_words[key].replace(first_vowel, "")
            needed_words[key] = new_word
        if last_consonant in key:
            new_word = needed_words[key].replace(last_consonant, "")
            needed_words[key] = new_word

    result = is_winner(needed_words)

    if result in needed_words.keys():
        print(f"Word found: {result}")
        break

if is_winner(needed_words) is None:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")