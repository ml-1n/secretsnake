import sys; import os; import random; import argparse
from importlib.resources import files

# load a wordlist from a file
def load_words(word_file):

    print("Loading word file: " + str(word_file))

    word_file = open(word_file).readlines()

    word_list = []

    for line in word_file:
        x = line.split()

        # parse it differently if it's a straight wordlist or if it has die-rolls on each line
        if len(x) > 1:
            word_list.append(x[1])
        
        else:
            word_list.append(x[0])

    
    return word_list

# generate the passphrase
def gen_passphrase(word_list, word_count):

    print("Word count: " + str(word_count))

    count = 0
    passphrase = ''

    while count < word_count:
        word_id = random.randint(0, len(word_list))
        word = word_list[word_id]
        passphrase += word
        count += 1

    print("Passphrase: " + passphrase)

def main():
    
    arg_parser = argparse.ArgumentParser(description='Generate a Diceware passphrase.')
    
    arg_parser.add_argument(
        '-c', '--count',
        dest = 'word_count',
        type = int,
        default = 6,
        help = 'the number of words the passphrase will contain (default: 6)')
    
    arg_parser.add_argument(
        '-f', '--file',
        dest = 'word_list',
        type = str,
        default = 'eff-large',
        choices = ['eff-large', 'eff-short', 'eff-short2'],
        help = 'the path to the list of possible words (options: eff-large, eff-short1, eff-short2) (default: eff-large)')

    args = arg_parser.parse_args()
 
    wordlist = files('dicewarecli').joinpath(args.word_list + ".wordlist")
    gen_passphrase(load_words(wordlist), args.word_count)

if __name__ == '__main__':
    
    main()
