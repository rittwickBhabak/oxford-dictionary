def print_phrasal_verbs(word, verbs):
    x = '='*(50+len(word))

    if not verbs:
        return
    if len(verbs)>0:
        print('Phrasal Verbs:')
        for verb in verbs:
            print(verb, end=', ')
        print()
        print(x)