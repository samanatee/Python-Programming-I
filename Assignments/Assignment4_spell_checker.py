'''
Created on Apr 25, 2018
@author: Samantha Hangsan
Assignment: 4
SPECS: 
- Develop spell checker program that spots and identifies misspelled words in a file 
- Prompt the user to enter a word and it should report the number of times the word appeared in the file
'''     
import string

def read_reference():
    reference_file = open('ref.txt', 'r')  # Read the reference file “ref.txt”
    reference_container = set()    # Create empty set to store words from reference file
    for row in reference_file: 
        row = row.strip('\n')
        reference_container.add(row)
    reference_file.close()
    return(reference_container)

def get_text():
    while True:
        try: 
            user_input = input('Enter the name of the file you want to spell check: ')
            # Return a file descriptor attached to the opened file
            text_file = open(user_input, 'r')
            return text_file
        except:
            print('Error! File not found!')

def spell_check(reference, word):
# Spellcheck each word and then display the words that were misspelled
    if word not in reference: 
        print('Mispelled word ' + repr(word))

def read_text(infile, reference):
    word_counter = {}    # Create empty dictionary to store the words the text file
    readlines = infile.readlines()
    for line in readlines: 
        line = line.translate(str.maketrans('', '', string.punctuation))    # Remove punctuation
        text = line.split()
        for word in text:
            if not word.isdigit():        # Remove digits
                word = word.lower()     # Convert to lowercase
                spell_check(reference, word)
                if word in word_counter:
                    word_counter[word] += 1
                else:
                 word_counter[word] = 1
    return(word_counter)
    infile.close()

def word_frequency(word_counter):
# Prompt the user to enter a word
    word = input('\nEnter a word to see how many times it was used in the file: ')
    word = word.lower()     # Convert to lowercase
# Return the number of times the word was used in the file
    if word in word_counter:
        frequency = word_counter[word]
    else: 
        frequency = 0
    print('The word ' + repr(word) + ' is repeated ' + str(frequency) + ' times.')

def main(): 
    reference_container = read_reference()
    text_file = get_text()
    word_counter = read_text(text_file, reference_container)
    word_frequency(word_counter)

if __name__ == '__main__':
    main()