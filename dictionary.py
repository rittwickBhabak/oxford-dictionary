from oxford_dictionary.get_response import meaning
from oxford_dictionary.get_senses import get_senses
from oxford_dictionary.print_meaning import print_meaning 
from oxford_dictionary.hear_pronounciaiton import hear_pronounciation
from oxford_dictionary.get_phrases_and_phrasal_verbs import get_phrasal_verbs, get_phrases
from oxford_dictionary.print_phrasal_verbs import print_phrasal_verbs
from oxford_dictionary.print_phrases import print_phrases
import sys

def main(word):
    response = meaning(word)
    senses = get_senses(response)
    phrases = get_phrases(response)
    phrasal_verbs = get_phrasal_verbs(response)
    if len(senses)==0:
        print('No results found.')
        return 
    
    print_meaning(word, senses)
    print_phrases(word, phrases)
    print_phrasal_verbs(word, phrasal_verbs)
    hear_pronounciation(senses)

if len(sys.argv)>1:
    word = sys.argv[1]
else:
    word = input('Enter the word: ')

while True:
    try:
        main(word)
        word = input('Enter next word: ')
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"ERROR: {str(e)}")
        input('Some error occoured.')

input('\nPress ENTER to exit')