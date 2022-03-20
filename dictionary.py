from oxford_dictionary.get_senses import get_senses
from oxford_dictionary.print_meaning import print_meaning 
from oxford_dictionary.hear_pronounciaiton import hear_pronounciation
import sys

def main(word):
    senses = get_senses(word)
    if len(senses)==0:
        print('No results found.')
        return 
    
    print_meaning(word, senses)
    hear_pronounciation(senses)

if len(sys.argv)>1:
    word = sys.argv[1]
else:
    word = input('Enter the word: ')

while True:
    try:
        main(word)
        word = input('Enter next word: ')
    except Exception as e:
        # print(f"ERROR: {str(e)}")
        input('Some error occoured.')
