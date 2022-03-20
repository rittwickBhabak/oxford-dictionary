def print_meaning(word, senses):
    x = '='*(50+len(word))
    y = '-'*(50+len(word))
    print(y)
    print(f"------------------------ {word.upper()} ------------------------")
    print(y)
    for sense in senses:
        definitions = sense.get('definitions')
        examples = sense.get('examples')
        if definitions:
            print('Definitions:')
            for index, definition in enumerate(definitions):
                print(f"{index+1}. {definition}")

        if examples:
            print('Examples:')
            for index, example in enumerate(examples):
                print(f"{index+1}. {example['text']}")
        print(x)