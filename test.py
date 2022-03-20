from oxford_dictionary.get_senses import get_senses
from oxford_dictionary.print_meaning import print_meaning 

import sys

if len(sys.argv)>1:
    word = sys.argv[1]
    try:    
        senses = get_senses(word)
        print_meaning(word, senses)
        input('Press ENTER to exit.')
    except Exception as e:
        print(f"ERROR: {str(e)}")
        input('Some error occoured. Press ENTER to EXIT.')
else:
    try:
        while True:
            word = input('Enter the word: ')
            senses = get_senses(word)
            print_meaning(word, senses)
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        input('Some error occoured. Press ENTER to EXIT.')