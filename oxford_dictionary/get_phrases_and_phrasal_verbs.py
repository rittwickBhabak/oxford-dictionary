import json 

def parse(response):
    all_phrasalVerbs = set()
    all_phrases = set()
    results = response.get('results')
    if results:
        for result in results:
            lexicalEntries = result.get('lexicalEntries')
            for lexicalEntry in lexicalEntries:
                phrasalVerbs = lexicalEntry.get('phrasalVerbs')
                phrases = lexicalEntry.get('phrases')

                if phrasalVerbs:
                    for phrasalVerb in phrasalVerbs:
                        text = phrasalVerb.get('text')
                        if text:
                            all_phrasalVerbs.add(text)
                
                if phrases:
                    for phrase in phrases:
                        text = phrase.get('text')
                        if text:
                            all_phrases.add(text)

    return (all_phrasalVerbs, all_phrases)

def get_phrases(response):
    phrasal_verbs, phrases = parse(response)
    if phrases:
        return list(phrases)

def get_phrasal_verbs(response):
    phrasal_verbs, phrases = parse(response)
    if phrasal_verbs:
        return list(phrasal_verbs)