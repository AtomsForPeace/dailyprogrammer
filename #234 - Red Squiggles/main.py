#!/usr/bin/env python


with open('enable1.txt', 'r') as file:
    woerterbuch = file.readlines()


test_words = (
    'accomodate', 'acknowlegement', 'arguemint', 'comitmment',
    'deductabel', 'depindant', 'existanse', 'forworde', 'herrass',
    'inadvartent', 'judgemant', 'ocurrance', 'parogative', 'suparseed',
    )


def spellchecker(test_word):
    for index, letter in enumerate(test_word):
        if not test_word[:index] in [wort[:index] for wort in woerterbuch]:
            test_word = test_word[:index] + '<' + test_word[index:]
            break
    return test_word


if __name__ == '__main__':
    for word in test_words:
        print spellchecker(word)
