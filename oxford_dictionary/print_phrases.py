from termcolor import cprint
import colorama
colorama.init()


def print_phrases(word, phrases):
    x = '='*(50+len(word))

    if not phrases:
        return 
    if len(phrases)>0:
        cprint('Phrases:', 'yellow')
        for phrase in phrases:
            print(phrase, end=', ')
        print()
        print(x)