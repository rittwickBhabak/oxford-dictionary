def print_meaning(word, senses):
    x = '='*(50+len(word))
    print(x)
    print(f"========================={word.upper()}=========================")
    print(x)
    for sense in senses:
        definitions = sense.get('definitions')
        examples = sense.get('examples')
        print('Definitions:')
        for index, definition in enumerate(definitions):
            print(f"{index+1}. {definition}")

        if examples:
            print('Examples:')
            for index, example in enumerate(examples):
                print(f"{index+1}. {example['text']}")
        print(x)