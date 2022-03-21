from termcolor import cprint

def print_meaning(word, senses):
    x = '='*(50+len(word))
    y = '-'*(50+len(word))
    print(y)
    print(f"------------------------ {word.upper()} ------------------------")
    print(y)
    for sense in senses:
        definitions = sense.get('definitions')
        examples = sense.get('examples')
        synonyms = sense.get('synonyms')
        if definitions:
            cprint('Definitions:', 'yellow')
            for index, definition in enumerate(definitions):
                print(f"{index+1}. {definition}")
        
        if synonyms:
            cprint('Synonyms:', 'yellow')
            for synonym in synonyms:
                print(synonym.get('text'), end=', ')
            print()

        if examples:
            cprint('Examples:', 'yellow')
            for index, example in enumerate(examples):
                print(f"{index+1}. {example['text']}")
        print(x)