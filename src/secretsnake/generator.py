import sys
import os
import random
import string


# generate the passphrase
def gen_passphrase(word_num, word_list, capitalize, special_char, verbose):

    count = 0
    passphrase = ''

    while count < word_num:
        word_id = random.randint(0, len(word_list))
        word = word_list[word_id]

        if capitalize:
            word = word.capitalize()

        if verbose:
            print('Word ' + str(count+1) + ': ' + word)

            if word_num - count == 1:
                print('\n')

        passphrase += word
        count += 1

    if special_char:
        passphrase = insert_special(passphrase)

    return passphrase

# insert a special character at a random position in a passphrase
def insert_special(passphrase):
    split_position = random.randint(0, len(passphrase) - 1)

    special_char = random.choice(string.punctuation + string.digits)

    return passphrase[:split_position] + special_char + passphrase[split_position:]
