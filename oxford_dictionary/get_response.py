import requests
from .get_key import CREDENTIALS, get_key

CREDENTIALS = get_key()
APP_ID = CREDENTIALS.get('app_id')
APP_KEY = CREDENTIALS.get('api_key')
language = "en-gb"

def write_output(word, response, debug):
    if not debug:
        return 
        
    with open(f"{word}.json", 'w', encoding='utf8') as f:
        f.write(str(response.text))

def meaning(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": APP_ID, "app_key": APP_KEY})
    debug = True
    write_output(word_id, r, debug)
    return r 

if __name__=="__main__":
    print(meaning('example'))