"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Use open function to open the file, file_path
    # Get text from file as a string and use read method
    # Return that

    text_file = open(file_path)
    return text_file.read()

# print(open_and_read_file('green-eggs.txt'))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    # Split input text string and store as variable, words
    # Loop over the range of length of list
    # Create a tuple of words[i] and words [i+1] and assign as a key
    # Create a value variable as assign as words[i+2]
    # Put the key and value we made into chains - chains[key] = [value]
    words = text_string.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        value = words[i+2]
        chains[key] = chains.get(key, [])
        # print(f'chains is {chains}')
        # print(f'chains[key] is {chains[key]}')
        chains[key].append(value)

    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
