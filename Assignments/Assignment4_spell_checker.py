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
	with open('ref.txt') as reference_file:	# automatically closes file
		reference_file.read()	# Read the reference file “ref.txt”
		reference_container = set()	# Create empty set to store words from reference file
		for row in reference_file: 
			row = row.strip('\n')
			reference_container.add(row)
		return reference_container
	

def get_text():
    while True:
        try: 
            user_input = input('Enter the name of the file you want to spell check: ')
            # Return a file descriptor attached to the opened file
            text_file = open(user_input, 'r')
            return text_file
        except:
            print('Error! File not found!')

def read_text(infile):
	text_container = {}	# Create empty dictionary to store the words the text file
	readlines = infile.readlines()
	for line in readlines: 
		line = line.translate(str.maketrans('', '', string.punctuation))	# Remove punctuation
		words = line.split()
		for words in words:
			if not words.isdigit():		# Remove digits
				print(words)
		# text_container[line] = 1
		# print(text_container)
	
    # Keys are the words in the file and values are the number of times the word is used in the file
    # Eliminate the punctuation when constructing the dictionary from the input file
    # If numbers are being use in the input file, they shouldn’t be spellchecked
	infile.close()

def spell_check():
	pass
# Spellcheck each word and then display the words that were misspelled

def word_counter():
	pass
# Prompt the user to enter a word 
# Return the number of times the word was used in the file

def main(): 
    reference_container = read_reference()
    text_file = get_text()
    read_text(text_file)
    # call word_counter()

if __name__ == '__main__':
    main()