from .get_response import meaning 
import json 

def get_senses(word):
    response = meaning(word)
    all_senses = []
    results = json.loads(response.text).get('results')
    if results:
        for result in results:
            lexicalEntries = result.get('lexicalEntries')
            for lexicalEntry in lexicalEntries:
                entries = lexicalEntry.get('entries')
                for entry in entries:
                    senses = entry.get('senses')
                    for sense in senses:
                        all_senses.append(sense)
    return all_senses 