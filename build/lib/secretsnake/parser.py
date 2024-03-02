import argparse
import sys

from secretsnake import generator
from importlib.resources import files # for data file inclusion in the package

def main():

    args = get_args()

    word_list = load_word_file(args.word_file)

    passphrase = generator.gen_passphrase(
        args.word_num,
        word_list,
        args.capitalize,
        args.special_char,
        args.verbose)
    
    if args.verbose:
        log('Word count: ' + str(args.word_num))
        log('Word list: ' + str(args.word_file))
        log('Capitalize: ' + str(args.capitalize))
        log('Special char: ' + str(args.special_char))
        log('Verbose: ' + str(args.verbose))
        log('')

        if len(passphrase) < 19:
            print('Warning: Passphrase is less than 19 characters long. Entropy may be sigificantly lower than needed.')

    log('Passphrase: ', end='')
    print(passphrase)

    sys.ou

        
def get_args():
    arg_parser = argparse.ArgumentParser(description='Generate a Diceware passphrase.')
    
    arg_parser.add_argument(
        '-n', '--num',
        dest='word_num',
        type=int,
        default=6,
        help='the number of words the passphrase will contain (default: 6)')
    
    arg_parser.add_argument(
        '-f', '--file',
        dest='word_file',
        type=str,
        default='eff-large',
        choices=['eff-large', 'eff-short', 'eff-short2'],
        help='the path to the list of possible words (default: eff-large)')

    arg_parser.add_argument(
        '-c', '--capitalize',
        action='store_true',
        dest='capitalize',
        help='capitalize the first letter of each word')

    arg_parser.add_argument(
        '-s', '--specialchar',
        action='store_true',
        dest='special_char',
        help='insert a special character or digit at a random location in the passphrase')

    arg_parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='verbose',
        help='output each word as they are generated')

    return arg_parser.parse_args()


# load a wordlist from a file
def load_word_file(word_file):

    word_file = files('secretsnake').joinpath(word_file + '.wordlist')
    word_lines = word_file.open('r').readlines()

    word_list = []

    for line in word_lines:

        # for debugging only
        # print(line)
        
        x = line.split()

        # parse it differently if it's a straight wordlist or if it has die-rolls on each line
        if len(x) > 1:
            word_list.append(x[1])
        
        else:
            word_list.append(x[0])     
    
    return word_list

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)