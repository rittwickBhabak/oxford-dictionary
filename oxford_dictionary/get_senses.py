from .get_response import meaning 
import json 

def get_senses(response):
    all_senses = []
    
    results = response.get('results')
    if results:
        for result in results:
            lexicalEntries = result.get('lexicalEntries')
            for lexicalEntry in lexicalEntries:
                entries = lexicalEntry.get('entries')
                for entry in entries:
                    track_urls = entry.get('pronunciations')
                    if track_urls:
                        if len(track_urls)>0:
                            track_url = track_urls[0].get('audioFile')
                    senses = entry.get('senses')
                    for sense in senses:
                        if track_urls and  track_url:
                            sense['track_url'] = track_url 
                        all_senses.append(sense)
    return all_senses 